SELECT * FROM products;

-- ======================= Применение функции ранжирования =============================

/* 01. Присвоить ранг продукта без пропусков значений в ранге от больше себестоимости к меньшей. 
       Вывести ТОП 10 продуктов product_name. */
WITH s AS (
    SELECT
        product_name,
        list_price,
        DENSE_RANK() OVER(ORDER BY standard_cost DESC) lp_dense_rank,
        RANK() OVER(ORDER BY standard_cost DESC) lp_rank
    FROM
        products
)
SELECT
    *
FROM
    s
WHERE
    lp_rank <= 10;


-- 02. Пронумеровать строки в таблице в зависимости от названия товара от A до Z.

SELECT
    product_name,
    RANK() OVER(ORDER BY product_name) pn_rank
FROM
    products;

/* 03. Разделить все продукты на 4 равных группы в зависимости от list_price. 
       Вывести имя продукта, list_price и номер группы.*/

SELECT
    product_name,
    list_price,
    NTILE(4) OVER(ORDER BY list_price) lp_rank
FROM
    products;




SELECT * FROM purchase_orders;

-- ============================ Работа с таблицей purchase_orders =============================

/* 01. Из таблицы purchase_orders для каждого поставщика supplier_id выведите дату создания заказа,
а также дату создания предыдущего заказа. Посчитайте разницу между этим датами в днях. */

SELECT
    supplier_id,
    creation_date,
    LAG(creation_date, 1, creation_date) OVER (
        PARTITION BY supplier_id
        ORDER BY
        creation_date
    ) cd_lag,
    DATEDIFF(
        creation_date, 
        LAG(creation_date, 1, creation_date) OVER (
            PARTITION BY supplier_id 
            ORDER BY creation_date
            )) cd_diff_days
FROM
    purchase_orders;


-- 02. Измените предыдущий запрос таким образом, чтобы узнать среднее время между двумя заказами.

WITH ordered_purchases AS (
    SELECT
        supplier_id,
        creation_date,
        LAG(creation_date) OVER (
            PARTITION BY supplier_id
        ORDER BY
            creation_date
        ) AS prev_creation_date,
        DATEDIFF(creation_date, LAG(creation_date) OVER (
            PARTITION BY supplier_id
            ORDER BY creation_date
        )) AS cd_diff_days
    FROM
        purchase_orders
)
SELECT
    *,
    AVG(cd_diff_days) OVER (
        PARTITION BY supplier_id
    ) AS cd_avg_diff_days
FROM
    ordered_purchases;
 
-- 03. Напишите аналогичный второму задания запрос, но с использованием функции LEAD. Сравните результаты.

WITH ordered_purchases AS (
    SELECT
        supplier_id,
        creation_date,
        LEAD(creation_date) OVER (
            PARTITION BY supplier_id
        ORDER BY
            creation_date
        ) AS prev_creation_date,
        DATEDIFF(LEAD(creation_date) OVER (
            PARTITION BY supplier_id
            ORDER BY creation_date
        ), creation_date) AS cd_diff_days
    FROM
        purchase_orders
)
SELECT
    *,
    AVG(cd_diff_days) OVER (
        PARTITION BY supplier_id
    ) AS cd_avg_diff_days
FROM
    ordered_purchases;

-- сравнение результатов
WITH ordered_purchases1 AS (
    SELECT
        id,
        LAG(creation_date) OVER (
            PARTITION BY supplier_id
        ORDER BY
            creation_date
        ) AS prev_creation_date,
        DATEDIFF(creation_date, LAG(creation_date) OVER (
            PARTITION BY supplier_id
            ORDER BY creation_date
        )) AS cd_diff_days
    FROM
        purchase_orders
),
ordered_purchases2 AS (
    SELECT
        id,
        LEAD(creation_date) OVER (
            PARTITION BY supplier_id
        ORDER BY
            creation_date
        ) AS prev_creation_date,
        DATEDIFF(LEAD(creation_date) OVER (
            PARTITION BY supplier_id
            ORDER BY creation_date
        ), creation_date) AS cd_diff_days
    FROM
        purchase_orders
),
res AS (
    SELECT
        po.supplier_id,
        po.creation_date,
        AVG(op1.cd_diff_days) OVER (
            PARTITION BY supplier_id
        ) AS cd_avg_diff_days1,
        AVG(op2.cd_diff_days) OVER (
            PARTITION BY supplier_id
        ) AS cd_avg_diff_days2
    FROM
        purchase_orders po
    JOIN ordered_purchases1 op1 ON
        po.id = op1.id
    JOIN ordered_purchases2 op2 ON
        po.id = op2.id
)
SELECT
    *,
    cd_avg_diff_days1 = cd_avg_diff_days2 same
FROM
    res;


/* 04. Найдите самую раннюю дату submitted_date для каждого менеджера created_by.
Решите данное задание использую оконные функции MIN и FIRST VALUE. Сравните результаты. */

SELECT
    created_by,
    min(submitted_date) sd_min
FROM
    purchase_orders
WHERE
    created_by IS NOT NULL
GROUP BY
    created_by;


SELECT DISTINCT 
    created_by,
    FIRST_VALUE(submitted_date) OVER(PARTITION BY created_by ORDER BY submitted_date) sd_min
FROM
    purchase_orders
WHERE
    created_by IS NOT NULL;
