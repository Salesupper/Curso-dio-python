CREATE TABLE Cor(
	idCor TINYINT IDENTITY(1,1),
	descricao VARCHAR(50) UNIQUE NOT NULL,
	CONSTRAINT pkIdCor PRIMARY KEY(idCor),
	CONSTRAINT uqDescricao UNIQUE(descricao)
);


CREATE TABLE Fornecedor(
	idFornecedor TINYINT IDENTITY(1,1),
	nome VARCHAR(50) UNIQUE NOT NULL,
	telefone VARCHAR(15),
	contato VARCHAR(20) NOT NULL,
	CONSTRAINT pkIdFornecedor PRIMARY KEY(idFornecedor),
	CONSTRAINT uqNome UNIQUE(nome)
);


CREATE TABLE Produto(
	idProduto TINYINT IDENTITY(1,1),
	codigo CHAR(6) UNIQUE NOT NULL,
	nome VARCHAR(50) UNIQUE NOT NULL,
	estoque SMALLINT,
	descontinuado bit,
	idFornecedor_produto TINYINT,
	idCor_produto TINYINT,
	CONSTRAINT pkProduto PRIMARY KEY(idProduto),
	CONSTRAINT uqCodigo UNIQUE(codigo),
	CONSTRAINT uqNomeProduto UNIQUE(nome),
	CONSTRAINT fkFornecedor FOREIGN KEY(idFornecedor_produto) REFERENCES Fornecedor(idFornecedor),
	CONSTRAINT fkCor FOREIGN KEY(idCor_produto) REFERENCES Cor(idCor)
);
