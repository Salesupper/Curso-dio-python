--ex 1
SELECT 
	o.orderid AS 'num_pedido',
	o.orderdate AS 'data_pedido',
	c.contactname AS 'nome_contato',
	c.country AS 'pais'
FROM Sales.Orders o 
JOIN Sales.Customers c 
ON o.custid = c.custid;

--ex 2
SELECT 
	o.orderdate AS 'data_pedido',
	c.contactname AS 'nome_contato',
	e.firstname,
	e.lastname, 
	e.country AS 'pais'
FROM Sales.Orders o
JOIN Sales.Customers c 
ON o.custid = c.custid 
JOIN HR.Employees e 
ON o.empid = e.empid 
WHERE e.country = 'UK';

--ex 3
SELECT 
	o.orderid,
	o.orderdate AS 'data_pedido',
	c.contactname AS 'nome_contato',
	c.country AS 'pais_cliente',
	e.firstname,
	e.lastname 
FROM Sales.Orders o
JOIN HR.Employees e 
ON o.empid = e.empid
JOIN Sales.Customers c
ON o.custid = c.custid 
WHERE c.country = 'Brazil'
ORDER BY o.orderdate DESC;

--ex 4
SELECT 
	o.orderid AS 'num_pedido',
	o.orderdate AS 'data_pedido',
	c.contactname AS 'nome_cliente',
	e.firstname+' '+e.lastname as 'nome_emp', 
	e.country as 'pais_emp',
	s.companyname as 'empresa_entrega'
FROM Sales.Orders o
JOIN HR.Employees e 
ON o.empid = e.empid
JOIN Sales.Customers c
ON o.custid = c.custid 
JOIN Sales.Shippers s 
ON o.shipperid = s.shipperid
WHERE e.country LIKE '%USA' AND 
s.companyname Like '%ETYNR' or 
s.companyname Like '%GVSUA'
ORDER BY o.orderid;



