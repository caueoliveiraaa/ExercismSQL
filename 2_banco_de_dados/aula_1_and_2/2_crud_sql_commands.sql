-- database: c:\Users\Leôncio Cauê\Desktop\apex_python_junho_2023\2_banco_de_dados\aula_1_and_2\mydatabase.db

-- SELECT é usado para selecionar dados de uma tabela
-- FROM é usado para indicar de qual tabela virão os dados
-- WHERE é onde passamos as condições, como o nome deve ser igual a john,
-- ou a idade tem que ser maior que 30, parecido com o if

-- Selecionar colunas específicas:
SELECT nome, email FROM usuarios
WHERE nome = 'John';

-- * é usado para selecionar todas as colunas
-- AND é usado quando queremos passar mais condições no SELECT, além do WHERE

-- Selecionar todas as colunas:
SELECT * FROM usuarios
WHERE nome = 'Bruce'
AND idade = 30
AND email = 'bruce@gmail.com';  

-- Ao subistituir o 'SELECT *' por 'DELETE', em vez de selecionarmos os dados
-- iremos deletar os mesmos

DELETE FROM usuarios
WHERE nome = 'Bruce';

-- Ao usar o UPDATE, estamos atualizando dados de uma tabela.
-- O SET, será responsável por nomes de colunas, e valores novos a inserir
-- Abaixo passamos a condição com o WHERE, especificando onde queremos realizar a alteração

UPDATE usuarios 
SET nome = 'Bryan' 
WHERE id = 1;

-- Podemos atualizar mais de uma coluna de uma vez

UPDATE usuarios 
SET nome = 'Bryan', idade = 70, email = 'bryan@gmail.com' 
WHERE id = 1;