

EXEC sp_help 'VendasAnuais'

DROP TABLE mes

SELECT *
FROM ano;

CREATE TABLE Ano(
	idAno TINYINT IDENTITY(1,1),
	ano SMALLINT,
	CONSTRAINT pkAno PRIMARY KEY (idAno)
);

CREATE TABLE Mes(
	idMes TINYINT IDENTITY(15,3),
	mes TINYINT,
	CONSTRAINT pkMes PRIMARY KEY (idMes)
);

CREATE TABLE Modelo(
	idModelo TINYINT IDENTITY(1,1),
	descricao VARCHAR(50),
	CONSTRAINT pkModelo PRIMARY KEY (idModelo)
);

CREATE TABLE Fabricante(
	idFabricante TINYINT IDENTITY(1,1),
	nome VARCHAR(50),
	cidade VARCHAR(50),
	endereco VARCHAR(100),
	uf CHAR(2),
	telefone VARCHAR(20),
	contato VARCHAR(50),
	CONSTRAINT pkFabricante PRIMARY KEY(idFabricante)
);

CREATE TABLE Veiculo(
	idVeiculo SMALLINT IDENTITY(1,1),
	descricao VARCHAR(50),
	valor DECIMAL(8,2),
	idModelo TINYINT,
	idFabricante TINYINT,
	idAnoFabricacao TINYINT,
	dataCompra DATE,
	CONSTRAINT pkVeiculo PRIMARY KEY(idVeiculo),
	CONSTRAINT fkVeiculo_Modelo FOREIGN KEY(idModelo) REFERENCES Modelo(idModelo),
	CONSTRAINT fkVeiculo_Fabricante FOREIGN KEY(idFabricante) REFERENCES Fabricante(idFabricante),
	CONSTRAINT fkVeiculo_Ano FOREIGN KEY(idAnoFabricacao) REFERENCES Ano(idAno)
);

CREATE TABLE VendasAnuais(
	idVendas SMALLINT IDENTITY(1,1),
	qtd SMALLINT,
	idVeiculo SMALLINT,
	idAnodaVenda TINYINT,
	idMesdaVenda TINYINT,
	CONSTRAINT pkVendasAnuais PRIMARY KEY(idVendas),
	CONSTRAINT fkVendas_Veiculo FOREIGN KEY(idVeiculo) REFERENCES Veiculo(idVeiculo),
	CONSTRAINT fkVendas_Ano FOREIGN KEY(idAnodaVenda) REFERENCES Ano(idAno),
	CONSTRAINT fkVendas_Mes FOREIGN KEY(idMesdaVenda) REFERENCES Mes(idMes)
);
