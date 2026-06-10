/* 1. Создайте хранимую процедуру get_department_id, которая
    принимает id сотрудника (IN-параметр), и возвращает id департамента
    (где работает сотрудник) через OUT-параметр. */

DROP PROCEDURE get_department_id;

CREATE PROCEDURE get_department_id (IN eid int, OUT did int)
SELECT department_id INTO did FROM employees WHERE employee_id = eid;

CALL get_department_id(120, @dep_id);
SELECT @dep_id;

/* 2. Создайте хранимую процедуру get_employee_age, которая
   принимает id сотрудника (IN-параметр)
   и возвращает его возраст через OUT-параметр. */

CREATE PROCEDURE get_employee_age(IN eid int, OUT ea int)
SELECT age INTO ea WHERE employee_id = eid;

CALL get_employee_age(120, @age);

SELECT @age; 

/* 3. Создайте хранимую процедуру increase_salary, которая
   принимает зарплату сотрудника (INOUT-параметр) и уменьшает ее на 10%. */


CREATE PROCEDURE decrease_salary(INOUT salary decimal(10,2))
SET salary = salary * 0.9;

SET @salary = 10000;

CALL decrease_salary(@salary);

SELECT @salary; 
