'''
To prepare for your MySQL aptitude test effectively before January 24th, here’s a study plan with resources, time allocation, and topics to focus on:

Study Plan Overview (Approx. 3-4 Days)
Day 1: Foundation and Basic Concepts (Approx. 1.5–2 hours)

Topics to cover:
Introduction to MySQL: Understand what MySQL is and its applications in databases.
Basic SQL Commands: SELECT, INSERT, UPDATE, DELETE.
Data Types in MySQL: INT, VARCHAR, DATE, etc.
Basic Filtering: WHERE clause, logical operators (AND, OR, NOT), and comparison operators (=, <>, >, <, BETWEEN, IN).
Resources:
W3Schools MySQL Tutorial
MySQL Documentation
Day 2: Intermediate SQL Queries (Approx. 2–2.5 hours)

Topics to cover:
JOINs: INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN (if applicable).
GROUP BY and HAVING: Aggregate functions like COUNT(), AVG(), SUM(), MIN(), MAX().
ORDER BY: Sorting results, both ascending and descending.
Subqueries: Subqueries in SELECT, WHERE, and FROM clauses.
Resources:
SQL Joins Explained
MySQL Aggregate Functions
Day 3: Advanced MySQL Features (Approx. 2 hours)

Topics to cover:
Indexes: Why they are important for query performance.
Normalization and Relationships: Primary and Foreign Keys, normalization rules (1NF, 2NF, 3NF).
Stored Procedures and Triggers (Basic Understanding).
Transactions: COMMIT, ROLLBACK, and isolation levels.
Resources:
MySQL Indexing
MySQL Transactions
Day 4: Practice and Mock Tests (Approx. 1.5–2 hours)

Topics to cover:
Take practice tests or quizzes to simulate the actual test environment.
Review tricky SQL problems and reattempt them if necessary.
Focus on time management during this practice session.
Resources:
HackerRank SQL Practice
LeetCode SQL Problems
MySQL Mock Test
Additional Preparation Tips:
Practice Writing Queries: The best way to prepare for an aptitude test is by writing queries, not just reading them. Use an online MySQL editor or XAMPP to run your queries and understand their behavior.
Review Test Format: If possible, check if there’s any sample test available or details about the types of questions (e.g., multiple-choice, coding problems, or theoretical questions).
Set a Time Limit: Since the test will take 25-35 minutes, ensure that you practice within that time frame during your mock tests. Focus on accuracy and speed.
Stay Calm and Focused: Ensure that you are well-rested before the test and have a stable internet connection.
Time Needed to Study:
Total Study Time: Approx. 7–8 hours across 3–4 days.
Breakdown:
Day 1: 1.5–2 hours (Basics)
Day 2: 2–2.5 hours (Intermediate concepts)
Day 3: 2 hours (Advanced concepts)
Day 4: 1.5–2 hours (Mock tests)
Final Preparation
Make sure you finish studying by January 23rd so that you can revise briefly the day before the test.
Have a clear plan to avoid interruptions during your test on January 24th.
Good luck with your preparation! If you need any help with specific topics, feel free to ask.

'''









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

** SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);

** SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);


** SELECT column_name(s)
FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE condition);

** CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    WHEN conditionN THEN resultN
    ELSE result
END;

INSERT INTO table2
SELECT * FROM table1
WHERE condition;

INSERT INTO table2 (column1, column2, column3, ...)
SELECT column1, column2, column3, ...
FROM table1
WHERE condition;

SHOW DATABASE;
usgned,signed ,zeroful attributes;
stored procedure, stored function;
trigger, events;
Mysql view; 
'''