--ex1
SELECT 5/2.0 AS 'Divisao';

--ex2
SELECT 200 + ((500/20) * 10.5) AS 'calculo';

--ex3
SELECT TOP 100 nome,eMail
FROM dbo.funcionario

--ex4 
SELECT nome +' '+sobrenome AS 'nome_completo'
FROM dbo.funcionario;

--ex5
SELECT matricula,nome,sobrenome,Salario,Bonus,(Salario + Bonus) AS 'salario_total'
FROM dbo.funcionario;

--ex4
SELECT DISTINCT cargo
FROM dbo.funcionario;

--ex5
SELECT nome,cargo,salario,salario + (salario * 0.07) AS 'salario_aumento'
FROM dbo.funcionario;