SELECT * FROM usuarios;

-- Selecionando o maior valor na coluna idade (MAX):
SELECT MAX(idade) FROM usuarios;


-- Selecionando o menor valor na coluna idade (MIN):
SELECT MIN(idade) FROM usuarios;

-- Selecionando a média da coluna idade usando AVG:
-- AVG = avarage, que é média em pt

SELECT avg(idade) FROM usuarios;

-- AS = como, traga a média como 'nome_da_coluna' com média
SELECT avg(idade) AS media_idade FROM usuarios;


-- COUNT = signifca contar, ele conta dados nas colunas
SELECT count(*) AS quantidade FROM usuarios;

SELECT count(email) FROM usuarios;

SELECT count(*) FROM usuarios
WHERE idade > 18;

SELECT count(*) FROM usuarios
WHERE idade < 18;

SELECT count(email) AS quantidade_final 
FROM usuarios
WHERE email IS NOT NULL;
-- IS NOT NULL serve para verificar campos/clunas que 
-- não estão vazios

INSERT INTO usuarios (nome, idade, email)
VALUES ('kaka', 25, NULL);

SELECT count(*) AS contador
FROM usuarios
WHERE email IS NULL;

-- LIKE = server para buscar palavras, ou partes de palavras
-- para usar o LIKE, precisamos usar % %

-- buscar nomes que começam em a
SELECT nome FROM usuarios
WHERE nome LIKE 'a%';

-- buscar nomes que terminam em a
SELECT nome FROM usuarios
WHERE nome LIKE '%a';

-- buscar nomes que tenham a letra a 
-- mas apenas se a letra a aparece no nome
SELECT nome FROM usuarios
WHERE nome LIKE '%a%';