sp_help Ano

--ex1
INSERT INTO Fabricante VALUES 
('Fiat','Rua Palmeiras, 108','Sao Paulo','SP','27452200'),
('GM','AV. Alcantara, 275','Porto Alegre','RS','27452200'),
('VW','Rua dos Alemaes, 731','Chapeco','SC','39911375')

SELECT idFabricante, Nome 
FROM Fabricante;

UPDATE Fabricante
SET cidade = 'Chapeco'
WHERE idFabricante = 12;

--ex2
SELECT *
FROM Modelo

INSERT INTO Modelo VALUES
('Standard'),
('Premium'),
('Executive')

UPDATE Modelo 
SET descricao = 'Standard'
WHERE idModelo = 10;

--ex3
SELECT *
FROM Veiculo

SELECT *
FROM Ano 

INSERT INTO Ano VALUES (2025),(2026),(2027),(2028)

INSERT INTO Veiculo 
(descricao,valor,dataCompra,idModelo,idFabricante,idAnoFabricacao) VALUES
('Artic',31200.00,'2026-04-17',10,10,17),
('Voltz',40000.00,'2027-03-30',12,11,19),
('Zeo',63500.00,'2030-08-20',11,12,20),
('Bjorn',75000.00,'2035-01-07',11,11,20),
('Duntzen',22730.00,'2028-07-04',10,10,18),
('Tungsten',55374.00,'2031-05-24',12,12,19);

--ex4
SELECT *
FROM VendasAnuais 

SELECT *
FROM Veiculo

SELECT *
FROM Mes 

SELECT *
FROM Ano 

INSERT INTO Ano VALUES (2029)

INSERT INTO VendasAnuais
(qtd,idVeiculo,idAnodaVenda,idMesdaVenda)VALUES
(50,122,21,48),
(100,122,21,27),
(20,122,21,24),
(435,123,21,33)









