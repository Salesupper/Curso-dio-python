SELECT * 
FROM [Customers] 

SELECT
	[ProductID],
	[Price],
	(Price / 2) AS Totprice
FROM
	[Products]

SELECT
	TOP 3 [Item],
	[Description] AS Descricao,
	[Who] AS Genero,
	[WholesaleCost] AS TotPrecoCusto
FROM
	[ProductDescriptions]

SELECT DISTINCT [FirstName] 
FROM [Employees] 

SELECT
	[Item],
	[Price]
FROM
	[Products]
WHERE
	[Price] BETWEEN 25 AND 150