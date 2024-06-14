CREATE TABLE viagens.usuarios(
	id INT,
	nome VARCHAR(255) NOT NULL COMMENT 'nome do usuario',
	email VARCHAR(100) NOT NULL UNIQUE COMMENT 'email do usuario',
	endereco VARCHAR(50) NOT NULL COMMENT 'endereco do usuario',
	data_nascimento DATE NOT NULL COMMENT 'data de nascimento do usuario'	
);

CREATE TABLE viagens.destinos(
	id INT,
	nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'nome do destino',
	descricao VARCHAR(255) NOT NULL COMMENT 'descrição do destino'
);

CREATE TABLE viagens.reservas(
	id INT COMMENT 'identificador de reserva',
	id_usuario INT COMMENT 'id_usuario que fez a reserva',
	id_destino INT COMMENT 'email do usuario',
	data_reserva DATE COMMENT 'data da reserva',
	status VARCHAR(255) DEFAULT 'pendente' COMMENT 'status da reserva'
);
