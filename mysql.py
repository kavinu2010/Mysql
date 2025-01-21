'''select * from customer;


Some of The Most Important SQL Commands
SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index


*** select column1, column2... From table_name

SELECT CustomerName, City, Country FROM Customers;


** SELECT DISTINCT column1, column2, ...FROM table_name;

select distinct city from customers;

SELECT COUNT(DISTINCT Country) FROM Customers;

** SELECT column1, column2, ..FROM table_name WHERE condition;
** Note: The WHERE clause is not only used in SELECT statements, it is also used in UPDATE, DELETE, etc.!

SELECT * FROM Customers WHERE Country = 'Mexico';

SELECT * FROM Customers WHERE CustomerID = 1;

SELECT * FROM Customers
WHERE City IN ('Paris','London');

SELECT * FROM Products WHERE Price <> 18;

SELECT * FROM Products
WHERE Price BETWEEN 50 AND 60;

SELECT * FROM Customers
WHERE City LIKE 's%';

** SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;

** SELECT column1, column2, ...
FROM table_name
WHERE condition1 OR condition2 OR condition3 ...;

SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;


** SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;


** INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);

** INSERT INTO table_name
VALUES (value1, value2, value3, ...);

** SELECT column_names
FROM table_name
WHERE column_name IS NULL;

** SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;

** UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;

** DELETE FROM table_name WHERE condition;

** SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;

SELECT * FROM Customers
LIMIT 3;

-- What if we want to select records 4 - 6 (inclusive)?

MySQL provides a way to handle this: by using OFFSET.

The SQL query below says "return only 3 records, start on record 4 (OFFSET 3)":

-- SELECT * FROM Customers
LIMIT 3 OFFSET 3;


** SELECT MIN(column_name)
FROM table_name
WHERE condition;

** SELECT MAX(column_name)
FROM table_name
WHERE condition;

SELECT MIN(Price) AS SmallestPrice
FROM Products;

SELECT MAX(Price) AS LargestPrice
FROM Products;

***   
LIKE Operator	Description
WHERE CustomerName LIKE 'a%'	Finds any values that start with "a"
WHERE CustomerName LIKE '%a'	Finds any values that end with "a"
WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position
WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position
WHERE CustomerName LIKE 'a_%'	Finds any values that start with "a" and are at least 2 characters in length
WHERE CustomerName LIKE 'a__%'	Finds any values that start with "a" and are at least 3 characters in length
WHERE ContactName LIKE 'a%o'	Finds any values that start with "a" and ends with "o"

SELECT * FROM Customers
WHERE CustomerName NOT LIKE 'a%';

** SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);

SELECT * FROM Customers
WHERE Country IN (SELECT Country FROM Suppliers);


** SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;


** SELECT column_name AS alias_name
FROM table_name;

** SELECT column_name(s)
FROM table_name AS alias_name;

---SELECT Orders.OrderID, Customers.CustomerName, Orders.OrderDate
FROM Orders
INNER JOIN Customers ON Orders.CustomerID=Customers.CustomerID;--

Supported Types of Joins in MySQL
INNER JOIN: Returns records that have matching values in both tables
LEFT JOIN: Returns all records from the left table, and the matched records from the right table
RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
CROSS JOIN: Returns all records from both tables
MySQL INNER JOIN  MySQL LEFT JOIN  MySQL RIGHT JOIN  MySQL CROSS JOIN

** SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;

** SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);

(For distinct value)
** SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;

** SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;






'''