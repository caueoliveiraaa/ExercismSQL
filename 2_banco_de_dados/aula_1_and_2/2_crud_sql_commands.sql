-- database: c:\Users\Leôncio Cauê\Desktop\apex_python_junho_2023\2_banco_de_dados\aula_1_and_2\mydatabase.db

-- SELECT é usado para selecionar dados, específicos ou não
-- de uma tabela no banco de dados

SELECT nome, idade
FROM usuarios
WHERE nome = 'Cauê' 
AND idade = 26;

-- WHERE passar condições para o SQL, como por exemplo
-- seleciona todos os nomes, onde (where) a idade
-- é maior que 18 (WHERE campo_idade > 18)

-- AND serve para extender as condições do WHERE


-- Selecionar TODAS as colunas de uma vez
SELECT * FROM usuarios
WHERE nome = 'Bruno'
AND idade > 15
AND id > 10;


-- Deletar dados das tabelas
DELETE FROM usuarios
WHERE id < 5;


-- Modificar dados na tabela
UPDATE usuarios
SET nome = 'test'
WHERE nome = 'Bryan';

-- Modificar mais de uma coluna de uma vez
UPDATE usuarios
SET nome = 'None', idade = 0, email = '00@00'
WHERE id > 19;