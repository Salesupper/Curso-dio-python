--ex1
SELECT *
FROM Sales.Orders
WHERE shipcity = 'Resende'

--ex2
SELECT *
FROM Sales.Orders
WHERE shipcountry = 'Brazil' AND shipcity in ('Sao Paulo','Rio de Janeiro')

--ex3
SELECT 
	COUNT(orderid) AS 'total_pedidos'
FROM Sales.Orders
WHERE shipcountry = 'Brazil' AND shipregion in ('RJ','SP')

--ex4
SELECT 
	COUNT(orderid) AS 'total_pedidos',
	SUM(freight) AS 'soma_frete',
	MIN(freight) AS 'menor_frete',
	MAX(freight) AS 'maior_frete',
	AVG(freight) AS 'media_frete'
FROM Sales.Orders
WHERE shipcountry = 'Brazil' AND shipregion in ('RJ','SP')

--ex5
SELECT 
	SUM(sd.unitprice) as 'soma_preço'
FROM Sales.Orders so 
JOIN Sales.OrderDetails sd 
ON so.orderid = sd.orderid
WHERE shipcountry = 'Brazil'

--ex6
	



