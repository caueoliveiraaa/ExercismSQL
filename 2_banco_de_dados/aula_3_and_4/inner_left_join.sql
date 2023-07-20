-- database: c:\Users\Leôncio Cauê\Desktop\apex_python_junho_2023\2_banco_de_dados\aula_3_and_4\mydatabase.db

-- Criar tabela Usuarios com mesmas colunas que Programadores
-- Inserir 10 linhas com dados válidos

create table if not exists Usuarios (
    id integer primary key,
    nome_usu text(40),
    idade_usu integer,
    email_usu text(40),
    tipo_conta_usu text(40),
    sal_usu double
);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Rodrigo', 32, 'digao@gmail.com', 'Premium', 5.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Marina', 28, 'ma@gmail.com', 'Free', 9.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Ana', 28, 'anna@gmail.com', 'Parcial', 4.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Adrián', 29, 'adrian@gmail.com', 'Premium', 6.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Cauê', 26, 'caue@gmail.com', 'Free', 1.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Elaine', 48, 'elaine@gmail.com', 'Parcial', 5.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Eduardo', 32, 'apple@gmail.com', 'Premium', 8.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Apex', 32, 'apex@gmail.com', 'Free', 6.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Eliot', 32, 'mr_robot@gmail.com', 'Free', 7.000);

insert into Usuarios (nome_usu, idade_usu, email_usu, tipo_conta_usu, sal_usu)
values ('Pro Way', 32, 'pro@gmail.com', 'Free', 17.000);


-- Obter uma lista dos programadores juntamente com os usuários 
-- correspondentes com base em seus endereços de email.

select Programadores.nome as nome_programador,
Usuarios.nome_usu as nome_usuario,
Programadores.email as email_bateu
from Programadores
inner join Usuarios
on Programadores.email = Usuarios.email_usu;

update Usuarios
set email_usu = 'crazy@gmail'
where nome_usu = 'Rodrigo';

-- O INNER JOIN é utilizado para combinar as tabelas,
-- ou seja, mostrar os dados de ambas, com filtros,
-- com base na coluna informada depois do 'ON'

-- Ex:
-- Realizando o mesmo com a idade:
select Programadores.nome as nome_programador,
Usuarios.nome_usu as nome_usuario,
Programadores.idade as idade_bateu
from Programadores
inner join Usuarios
on Programadores.idade = Usuarios.idade_usu;

-- Agora, vamos supor que você deseja obter uma lista de todos 
-- os programadores e, se houver, o nome do usuário correspondente
-- com base no endereço de email

select Programadores.nome as nome_programador,
Usuarios.nome_usu as nome_usuario
from Programadores 
left join Usuarios
on Programadores.email = Usuarios.email_usu;
 
-- |--- EX 2 ---|
-- Criar tabela Contatos com mesmas colunas que Usuarios + coluna telefone (e outras se desejado)
-- Insira 20 linhas na tabela Contatos e repita o exercícios anterior
-- trocando a tabela usuarios pela tabela contatos

-- Criar tabele Contatos
create table if not exists Contatos (
    id integer primary key,
    nome text(40),
    idade integer,
    email text(40),
    salario double
);

-- Inserir dados em Contatos
insert into Contatos (nome, idade, email, salario)
values ('Bryan', 19, 'exemplo@', 2.555),
('Bruno', 21, 'bruno@gmail', 3.458),
('Cauê', 26, 'caue@gmail', 4.698);

-- Repetir exercicios acima com left e inner join
-- trocando a tabela Usuarios por Contatos recem criada

-- inner join:
select Programadores.nome as nome_programador,
Contatos.nome as nome_contato,
Programadores.idade as idade_bateu
from Programadores
inner join Contatos
on Programadores.idade = Contatos.idade;

-- left join:
select Programadores.nome as nome_programador,
Contatos.nome as nome_contato,
Programadores.idade as idade_bateu
from Programadores
left join Contatos
on Programadores.idade = Contatos.idade;

alter table Usuarios
add column ativo boolean;

-- Exemplo de como manipular boolean
insert into Contatos (nome, idade, email, salario, verdade)
values ('aa', 1, 'aaa', 2525.4, True);


-- Agora, suponha que você queira obter uma lista dos Usuarios juntamente 
-- com os contatos correspondentes com base no id.
-- Vamos inserir a coluna ativo em ambas as tabelas do tipo boolean (pesquisar como inserir boolean)
-- Metade das linhas das duas tabelas tem que estar com o ativo sendo true, e a outra metade false
-- A consulta deve retornar apenas os usuarios que possuem um id na tabela 
-- contatos correspondente ao id da tabela usuarios.
-- Após o ON, adicione um where no final para adicionar ao filtro também
-- apenas as idades que são maiores que 18 e menores que 30
-- No Final ordene por nome.


select * from Contatos;

update Usuarios
set ativo = True
where id < 3;


select Usuarios.nome_usu as nome_usuario,
Contatos.nome as nome_contato,
Usuarios.id as id_bateu
from Usuarios inner join Contatos
on Usuarios.id = Contatos.id
where Usuarios.idade_usu between 18 and 30
and Contatos.idade between 18 and 30
order by Usuarios.nome_usu asc;