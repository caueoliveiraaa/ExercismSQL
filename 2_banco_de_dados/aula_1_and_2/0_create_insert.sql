-- database: c:\Users\Leôncio Cauê\Desktop\apex_python_junho_2023\2_banco_de_dados\aula_1_and_2\mydatabase.db

-- Use the ▷ button in the top right corner to run the entire file.

-- 1 - Criar uma tabela
-- PRIMARY KEY:
-- Auto incrementa o valor que está no campo
-- Força o campo a não ter valor nulo
-- Garantir que cada usuário tenha um valor único

-- IF NOT EXISTS:
-- Garante que a tabela apenas será criada
-- caso uma tabela com o nome informado não exista!

CREATE TABLE IF NOT EXISTS usuarios (
    -- Campo do tipo inteiro, com chave primária
    id INTEGER PRIMARY KEY,
    -- TEXT é usado para campos do tipo string
    nome TEXT(100),
    -- INTEGER é usado para campos com números inteiros
    idade INTEGER,
    -- O último campo não leva vírgula
    email TEXT(100)
);

-- 2 - Inserindo dados na tabela criada:
-- INSERT INTO é o comando SQL para inserir dados nas tabelas
INSERT INTO usuarios (nome, idade, email)
-- É seguido pela palavra VALUES que armazena os valores nas colunas
VALUES ('Bryan', 25, 'bryan@gmail.com');

-- Inserindo mais dados na tabela:
INSERT INTO usuarios (nome, idade, email)
VALUES ('Cauê', 26, 'caue@gmail.com');

INSERT INTO usuarios (nome, idade, email)
VALUES ('Bruno', 28, 'bruno@gmail.com');

INSERT INTO usuarios (nome, idade, email)
VALUES ('Amanda', 14, 'amanda@gmail.com');

INSERT INTO usuarios (nome, idade, email)
VALUES ('Jim', 5, 'jim@gmail.com');


-- 3 - Alterando tebelas:
-- ALTER TABLE é usadado para alterar tabelas
-- RENAME TO que renomeia a tabela

ALTER TABLE usuarioss
RENAME TO usuarios;

-- ADD COLUMN adiciona uma coluna
ALTER TABLE usuarios
ADD COLUMN coluna_nova;

-- DROP COLUMN 
ALTER TABLE usuarios
DROP COLUMN coluna_nova;


-- 4 Resetando tabelas
-- DELETE FROM deleta todos os dados
-- da tabela se não for passado uma
-- condição específica.
-- VACUUM - zerar o primary key

DELETE FROM usuarios;

-- 5 Destruindo tabelas:
DROP TABLE usuarios;