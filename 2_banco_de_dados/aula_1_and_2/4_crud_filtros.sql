-- database: c:\Users\Leôncio Cauê\Desktop\apex_python_junho_2023\2_banco_de_dados\aula_1_and_2\mydatabase.db

select * from usuarios;

-- Selecionando o maior valor na coluna idade (MAX):
select max(idade) from usuarios;


-- Selecionando o menor valor na coluna idade (MIN):
select min(idade) from usuarios;

-- Selecionando a média da coluna idade usando AVG:
-- AVG = avarage, que é média em pt

select avg(idade) from usuarios;

-- AS = como, traga a média como 'nome_da_coluna' com média
select avg(idade) as media_idade from usuarios;


-- COUNT = signifca contar, ele conta dados nas colunas
select count(*) as quantidade from usuarios;

select count(email) from usuarios;

select count(*) from usuarios
where idade > 18;

select count(*) from usuarios
where idade < 18;

select count(email) as quantidade_final 
from usuarios
where email is not null;
-- IS NOT NULL serve para verificar campos/clunas que 
-- não estão vazios

insert into usuarios (nome, idade, email)
values ('kaka', 25, null);

select count(*) as contador
from usuarios
where email is null;

-- LIKE = server para buscar palavras, ou partes de palavras
-- para usar o LIKE, precisamos usar % %

-- buscar nomes que começam em a
select nome from usuarios
where nome like 'a%';

-- buscar nomes que terminam em a
select nome from usuarios
where nome like '%a';

-- buscar nomes que tenham a letra a 
-- mas apenas se a letra a aparece no nome
select nome from usuarios
where nome like '%a%';