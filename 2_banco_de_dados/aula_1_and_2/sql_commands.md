# Criando banco de dados:

    CREATE TABLE IF NOT EXISTS nome_tabela (
        id INTEGER PRIMARY KEY,
        coluna_nome TEXT(100),
        coluna_email TEXT(100),
        coluna_idade INTEGER
    )

# Inserindo dados:

    INSERT INTO nome_tabela (coluna_nome, coluna_idade, coluna_email)
    VALUES ('Bot', 100, 'bot@exemplo.com');

# Selecionando dados:

    SELECT * FROM nome_tabela

    SELECT * FROM nome_tabela
    WHERE coluna_idade > 18;
   
# Atualizando dados:

    UPDATE nome_tabela 
    SET coluna_nome = 'AI' 
    WHERE id = 1;

    UPDATE nome_tabela 
    SET coluna_nome = 'Robot', coluna_idade = 200, coluna_email = 'robot@gmail.com' 
    WHERE coluna_nome = 'AI';

# Deletando dados:

    DELETE FROM nome_tabela
    WHERE id = 1;

    DELETE FROM nome_tabela
    WHERE coluna_idade < 5;

# Resetando tabela:

    DELETE FROM nome_tabela
    VACUUM;

# Alterando nome da tabela:

    ALTER TABLE nome_tabela
    RENAME TO nome_tabela_novo;

# Incluir colunas:

    ALTER TABLE usuarios
    ADD COLUMN coluna_nova TEXT(40);

# Remover colunas

    ALTER TABLE nome_tabela
    DROP COLUMN coluna_nova;

# Deletando tabela:

    DROP TABLE nome_tabela;

# Filtandro com MIN e MAX:
    SELECT MAX(coluna_idade) FROM nome_tabela;

    SELECT MIN(coluna_idade) FROM nome_tabela;

# Filtandro com AVG e COUNT:

    SELECT coluna_idade, AVG(coluna_idade) FROM nome_tabela

    SELECT coluna_idade, COUNT(*) FROM nome_tabela

# Filtandro com WHERE, AND e LIKE:

    SELECT * FROM nome_tabela
    WHERE coluna_nome LIKE 'A%';
    
    SELECT * FROM usuarios
    WHERE coluna_nome LIKE '%son'
    AND coluna_email IS NOT NULL;

    SELECT * FROM usuarios
    WHERE coluna_email LIKE '%gmail%'
    AND coluna_idade > 15;

# Ordenando colunas:

    SELECT * FROM nome_tabela
    ORDER BY coluna_nome ASC;
    
    SELECT * FROM nome_tabela
    ORDER BY coluna_idade DESC;
    
# Agrupando colunas:

    SELECT coluna_idade, COUNT(*) FROM nome_tabela
    GROUP BY coluna_idade;

    SELECT coluna_idade, AVG(coluna_idade) FROM nome_tabela
    GROUP BY coluna_idade;

    
