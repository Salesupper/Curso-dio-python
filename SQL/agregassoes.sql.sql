--ex1
SELECT COUNT(idVendas) AS 'totalVendas'
FROM GLS.VendasAnuais;

--ex2
SELECT SUM(qtd) AS 'qtdTotal'
FROM GLS.VendasAnuais;

--ex3
SELECT 
	MIN(qtd) AS 'qtdMenor',
	AVG(qtd) AS 'qtdMedia',
	MAX(qtd) AS 'qtdMax'
FROM GLS.VendasAnuais;

--ex4
SELECT 
	a.ano,
	SUM(v.qtd) AS 'vendasAno'
FROM VendasAnuais v
JOIN Ano a ON v.idAnodaVenda = a.idAno
GROUP BY a.ano
ORDER BY a.ano DESC

--ex5
SELECT *
FROM Modelo

SELECT 
	va.idVendas,
	SUM(va.qtd) as 'vendasAno',
	ve.descricao,
	mo.descricao
FROM VendasAnuais va
JOIN Veiculo ve ON va.idVeiculo = ve.idVeiculo
JOIN Modelo mo ON ve.idModelo = mo.idModelo
WHERE ve.descricao = 'CG 125' AND mo.descricao = 'STD'
GROUP BY 
	va.idVendas,
	ve.descricao,
	mo.descricao
ORDER BY va.idVendas

