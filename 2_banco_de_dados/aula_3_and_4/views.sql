-- database: c:\Users\Leôncio Cauê\Desktop\apex_python_junho_2023\2_banco_de_dados\aula_3_and_4\mydatabase.db


-- Criou uma view
create view SelectProgramadores as
select id, nome, idade, email, linguagem_de_programacao
from Programadores;

-- Chamou a view
select * from SelectProgramadores;

-- Deletou a view
drop view SelectProgramadores;

-- Criando uma view nova
create view ProgramadoresUsuariosEmailMatch as 
select Programadores.nome as Programador,
Programadores.email as EmailMatch,
Usuarios.nome_usu as Usuario
from Programadores inner join Usuarios
on Programadores.email = Usuarios.email_usu
where nome is not null
order by nome asc;


-- Chamar a view nova
select * from ProgramadoresUsuariosEmailMatch;
