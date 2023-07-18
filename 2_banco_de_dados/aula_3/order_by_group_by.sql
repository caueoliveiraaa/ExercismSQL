-- database: c:\Users\Leôncio Cauê\Desktop\apex_python_junho_2023\2_banco_de_dados\aula_3\mydatabase.db

CREATE TABLE IF NOT EXISTS Programadores (
    id INTEGER PRIMARY KEY,
    nome TEXT(40),
    idade INTEGER,
    email TEXT(40)
);


SELECT * FROM Programadores;

-- Revisão:
-- CREATE, DROP, DELETE, INSERT, WHERE, LIKE
-- SELECT, AND, COUNT, UODATE, MAX, MIN, AVG.

-- Deletar uma tela
DROP TABLE Programadores;




-- Inserir valores
INSERT INTO Programadores (nome, idade, email)
VALUES ('Eliot', 25, 'mr_robot@hacker.tor');

INSERT INTO Programadores (nome, idade, email)
VALUES ('Darlene', 23, 'darlene_robot@hacker.tor');

INSERT INTO Programadores (nome, idade, email)
VALUES ('Tyrell Wellic', 25, 'evil_corp@hacker.tor');

INSERT INTO Programadores (nome, idade, email)
VALUES ('Angela', 25, 'moss@hacker.tor');

INSERT INTO Programadores (nome, idade, email)
VALUES ('Sheila', 25, 'sheila@hacker.tor');


-- Atualizar dados
UPDATE Programadores
SET nome = 'Bruno', idade = 60, email = 'bruno@gmail.com'
WHERE nome = 'Eliot'
AND id = 1;

SELECT id, nome, idade, email FROM Programadores
WHERE nome = 'Bruno';

ALTER TABLE Programadores
ADD COLUMN linguagem_de_programacao TEXT(40);

-- Inserir as linguagens de programação manulamente para
-- cada linha da tabela

UPDATE Programadores 
SET linguagem_de_programacao = ''
WHERE id = 5;


-- Buscar os valores min e max, de colunas
SELECT MAX(id) AS id_maior,
MIN(idade) AS idade_menor
FROM Programadores;


SELECT ROUND(AVG(idade), 2) AS media_idade
FROM Programadores;


-- Buscar palavras nos baseando em um texto aleatório

-- Palavras que começam com B
SELECT * FROM Programadores
WHERE nome LIKE 'B%';

SELECT * FROM Programadores
WHERE nome LIKE '%a';

SELECT * FROM Programadores
WHERE nome LIKE '%ei%';


-- ORDER BY = Ordene por

SELECT * FROM Programadores
ORDER BY idade DESC;

SELECT * FROM Programadores
ORDER BY idade ASC;

SELECT * FROM Programadores
ORDER BY nome ASC;

SELECT * FROM Programadores
ORDER BY nome DESC;


-- Exercício
-- Ordene a tabela programadores
-- por todas as colunas, usando tanto DESC e ASC

SELECT nome FROM Programadores
ORDER BY nome DESC;

SELECT nome FROM Programadores
ORDER BY nome ASC;

SELECT idade FROM Programadores
ORDER BY idade DESC;

SELECT idade FROM Programadores
ORDER BY idade ASC;

SELECT email FROM Programadores
ORDER BY email DESC;

SELECT email FROM Programadores
ORDER BY email ASC;

SELECT nome FROM Programadores
ORDER BY nome DESC;

-- GROUP BY = Agrupe por
SELECT *, COUNT(idade) AS quantidade_idade
FROM Programadores
WHERE idade > 18
GROUP BY idade;

SELECT COUNT(linguagem_de_programacao) AS total_python
FROM Programadores
WHERE linguagem_de_programacao = 'Java'
GROUP BY linguagem_de_programacao;



--  |--##-- EX: --##--|

-- Criar a coluna salario_dev na tabela Programadores e inserir salários diferentes
-- para todos as linhas.

-- Em seguida, selecionar os dados ordenando por id
 
-- Mostrar a média da coluna salario_dev 

-- Criar mais 5 colunas em uma das tabelas

-- inserir os dados manualmente com update nome_tabela set 

-- Selecionar a maior idade, e o menor id da tabela Programadores

-- Selecionar todas as colunas da tabela Programadores e ordenar pelo nome em ordem aufabética

-- Selecionar a idade da tabela Programadores, agrupando pela idade 
-- mostrando a mesma como total_idade_grup apenas onde a idade é maior ou igual a 18

-- Ordenar a tabela Programadores e ordenando por id

-- Homework:
-- Criar uma tabela nova, inserir 20 linhas e 8 colunas na tabela
-- Refazer todos os exercícios desse arquivo com a tabela criada