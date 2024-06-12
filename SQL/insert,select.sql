INSERT INTO usuarios (id,nome,email,endereco,data_nascimento) VALUES
(1, 'Ana Silva', 'ana.silva@email.com', 'Rua das Flores, 123', '1990-05-15'),
(2, 'Carlos Pereira', 'carlos.pereira@email.com', 'Avenida Brasil, 456', '1985-07-20'),
(3, 'Beatriz Santos', 'beatriz.santos@email.com', 'Praça da Liberdade, 789', '1992-10-30'),
(4, 'Daniel Costa', 'daniel.costa@email.com', 'Rua da Paz, 101', '1988-01-22'),
(5, 'Fernanda Lima', 'fernanda.lima@email.com', 'Travessa da Alegria, 202', '1995-03-18'),
(6, 'Eduardo Almeida', 'eduardo.almeida@email.com', 'Avenida das Nações, 303', '1987-09-14'),
(7, 'Gabriela Rocha', 'gabriela.rocha@email.com', 'Rua do Sol, 404', '1991-12-25'),
(8, 'Henrique Souza', 'henrique.souza@email.com', 'Avenida Central, 505', '1989-06-06'),
(9, 'Isabela Martins', 'isabela.martins@email.com', 'Rua Nova, 606', '1993-08-11'),
(10, 'João Oliveira', 'joao.oliveira@email.com', 'Travessa do Campo, 707', '1986-11-19');

INSERT INTO destinos (id,nome,descricao) VALUES
(1, 'Paris', 'A cidade das luzes, conhecida pela sua rica história e cultura.'),
(2, 'Tóquio', 'A capital do Japão, famosa pela sua modernidade e cultura tradicional.'),
(3, 'Nova York', 'A cidade que nunca dorme, conhecida por seus arranha-céus e diversidade cultural.'),
(4, 'Rio de Janeiro', 'Famosa por suas praias deslumbrantes e o Carnaval.'),
(5, 'Londres', 'A capital do Reino Unido, conhecida por seus marcos históricos como o Big Ben e a Torre de Londres.'),
(6, 'Sydney', 'A maior cidade da Austrália, famosa pela sua Opera House e praias.'),
(7, 'Roma', 'A capital da Itália, conhecida por sua história antiga e marcos como o Coliseu e o Vaticano.'),
(8, 'Bangkok', 'A capital da Tailândia, famosa por seus templos ornamentados e vida noturna vibrante.'),
(9, 'Barcelona', 'Uma cidade vibrante na Espanha, conhecida pela arquitetura de Gaudí e suas praias.'),
(10, 'Dubai', 'Uma cidade moderna nos Emirados Árabes Unidos, conhecida por seus arranha-céus e luxo.');

INSERT INTO reservas (id,id_usuario,id_destino,data_reserva,status) VALUES
(1, 1, 1, '2024-06-01', 'Confirmada'),
(2, 2, 2, '2024-06-02', 'Pendente'),
(3, 1, 3, '2024-06-03', 'Cancelada'),
(4, 4, 4, '2024-06-04', 'Confirmada'),
(5, 5, 5, '2024-06-05', 'Pendente'),
(6, 6, 6, '2024-06-06', 'Confirmada'),
(7, 7, 7, '2024-06-07', 'Cancelada'),
(8, 8, 8, '2024-06-08', 'Confirmada'),
(9, 9, 9, '2024-06-09', 'Pendente'),
(10, 10, 10, '2024-06-10', 'Confirmada');

SELECT *
FROM destinos 