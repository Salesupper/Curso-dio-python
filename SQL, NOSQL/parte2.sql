SELECT
	AVG([Quantity]) AS MediaQnt,
	STDEV([Quantity]) AS DesvioItem
FROM
	[Orders];
	
SELECT
	[Item],
	AVG([Price]) AS PMedio
FROM
	[Products]
GROUP BY
	[Item]
HAVING
	AVG([Price]) > 50
ORDER BY
	AVG([Price]);

SELECT
	[Department],
	AVG([Salary]) AS SalarioMedio
FROM
	[Employees]
GROUP BY
	[Department]
ORDER BY
	[Department] ASC

SELECT
	State,
	COUNT(*) AS QntClientes
FROM
	[Customers]
GROUP BY
	[State]






