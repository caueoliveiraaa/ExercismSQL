-- database: c:\Users\Leôncio Cauê\Desktop\apex_python_junho_2023\2_banco_de_dados\aula_1_and_2\mydatabase.db

-- 1 - Criando tabelas:
-- PRIMARY KEY:
-- Auto incrementa o valor que está no campo
-- Força o campo a não poder ter um valor null
-- Garante que cada usuário terá um valor único

-- IF NOT EXISTS:
-- Garante que a tabela apenas será criada
-- caso uma tabela com o nome usuarios não exista

CREATE TABLE IF NOT EXISTS usuarioss (
    -- Campo do tipo int com chave primária
    id INTEGER PRIMARY KEY,
    -- Text é usando para campos str
    nome TEXT(100),
    -- INTEGER é usando para campos do tipo int
    idade INTEGER,
    -- A última coluna da tabela não precisa de vírgula 
    email TEXT(100)
);

-- 2 - Inserindo dados em tabelas:
-- INSERT INTO é o comando SQL para inserir dados em uma tabela
INSERT INTO usuarioss (nome, idade, email)
-- Ele é seguido pelo VALUE que armazena os valores a serem armazenados
VALUES ('John', 30, 'john@exemplo.com');

-- Inserindo mais dados na tabela
INSERT INTO usuarioss (nome, idade, email)
VALUES ('Bruce', 36, 'bruce@exemplo.com');

INSERT INTO usuarioss (nome, idade, email)
VALUES ('Paul', 36, 'paul@exemplo.com');

INSERT INTO usuarioss (nome, idade, email)
VALUES ('Brock', 36, 'bro@exemplo.com');

-- 3 - Alterando tabelas:
-- ALTER TABLE altera uma tabela!
-- RENAME TO renomeia a tabela
ALTER TABLE usuarioss
RENAME TO usuarios;

-- ADD COLUMN adiciona uma coluna
ALTER TABLE usuarios
ADD COLUMN coluna_nova TEXT;

-- DROP COLUMN remove uma coluna
ALTER TABLE usuarios
DROP COLUMN coluna_nova;

-- 4 - Resetando tabelas:
-- DELETE FROM deleta todos os rows (linhas) da tabela
DELETE FROM usuarios;
-- VACUUM vai resetar a contabilização do PRIMARY KEY
-- Ele deve ser colocado logo após o comando acima
VACUUM;

-- 5 - Deletando tabelas:

-- DROP TABLE deleta uma tabela permanentemente
DROP TABLE usuarios;
