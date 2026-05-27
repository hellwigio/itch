-- 01. Для каждого product_id выведите inventory_id а также предыдущий и последующей inventory_id по убыванию quantity.
SELECT * FROM order_details;

SELECT
    product_id,
    inventory_id,
    LAG(inventory_id) OVER(
        PARTITION BY product_id 
        ORDER BY quantity DESC
    ) AS ii_prev,
    LEAD(inventory_id) OVER(
        PARTITION BY product_id 
        ORDER BY quantity DESC
    ) AS ii_next
FROM
    order_details;

/* 02. Выведите максимальный и минимальный unit_price для каждого order_id с помощью функции FIRST_VALUE().
       Выведите order_id и полученные значения. */

-- оконные функции
SELECT DISTINCT 
    order_id,
    FIRST_VALUE(unit_price) OVER (
        PARTITION BY order_id
    ORDER BY
        unit_price DESC
    ) up_max,
    FIRST_VALUE(unit_price) OVER (
        PARTITION BY order_id
    ORDER BY
        unit_price ASC
    ) up_min
FROM
    order_details;


-- группировка
SELECT 
    order_id,
    max(unit_price) up_max,
    min(unit_price) up_min
FROM
    order_details
GROUP BY
    order_id;

/* 03. Выведите order_id и столбец с разницей между unit_price для каждого заказа и минимальным unit_price в рамках одного заказа.
! Задачу решить двумя способами - с помощью FIRST_VALUE() и MIN().*/

-- FIRST_VALUE
SELECT
    order_id,
    unit_price - FIRST_VALUE(unit_price) OVER (
        PARTITION BY order_id
    ORDER BY unit_price ASC
    ) up_diff_min_cur
FROM
    order_details;

-- MIN
SELECT 
    order_id,
    unit_price - min(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price ASC) up_diff_min_cur
FROM
    order_details; 


-- 04. Присвойте ранг каждой строке, используя RANK() по убыванию quantity.
SELECT 
    order_id,
    unit_price - min(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price ASC) up_diff_min_cur,
    quantity,
    dense_rank() over(ORDER BY quantity desc) rnk
FROM
    order_details; 

-- 05. Из предыдущего запроса выберите только строки с рангом до 10 включительно.

WITH t AS(
SELECT 
    order_id,
    unit_price - min(unit_price) OVER (PARTITION BY order_id ORDER BY unit_price ASC) up_diff_min_cur,
    quantity,
    dense_rank() over(ORDER BY quantity desc) rnk
FROM
    order_details
) SELECT * FROM t WHERE rnk <= 10;


