--ex1
SELECT 
	productid, 
	productname,
	unitprice
FROM Production.Products
WHERE unitprice >= 19 AND unitprice <= 22;

SELECT 
	productid, 
	productname,
	unitprice
FROM Production.Products
WHERE unitprice BETWEEN 19 AND 22;

--ex2
SELECT 
	productid,
	productname,
	unitprice
FROM Production.Products
WHERE unitprice = 10 OR unitprice = 18 OR unitprice = 21.35;

SELECT 
	productid,
	productname,
	unitprice
FROM Production.Products
WHERE unitprice IN (10,18,21.35);

--ex3
SELECT 
	empid,
	titleofcourtesy,
	(firstname +' '+ lastname) AS complete_name,
	birthdate
FROM HR.Employees 
WHERE birthdate BETWEEN '1947' AND '1966';

SELECT 
	firstname,
	birthdate 
FROM HR.Employees;

--ex4
SELECT 
	firstname,city,
	region,country
FROM HR.Employees
WHERE city = 'Seattle' or country = 'UK';

--ex5
SELECT 
	empid,
	firstname,
	hiredate
FROM HR.Employees 
WHERE YEAR(hiredate) = '2002' OR YEAR(hiredate) = '2004';
   
--ex6
SELECT TOP 20 *
FROM Sales.Customers 
ORDER BY custid DESC;

--ex7
SELECT DISTINCT country
FROM Sales.Customers;

SELECT 
	custid,contactname,
	city,country
FROM Sales.Customers
WHERE country IN ('Argentina','Brazil','Venezuela')
ORDER BY country;

--ex8
SELECT 
	custid,contactname,fax  
FROM Sales.Customers 
WHERE fax IS NOT NULL 
ORDER BY custid DESC; 

--ex9
SELECT 
	custid,contactname,
	city,country,region 
FROM Sales.Customers 
WHERE region IS NULL 
ORDER BY country ASC, city DESC







