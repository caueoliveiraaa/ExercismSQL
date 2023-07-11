# No começo do arquivo realizamos os imports
# Usar o comando   pip install sqlite3   para instalar o sqlite no Python
import sqlite3
# Bibliotecas são códigos prontos para serem executados
# realizando conexões com base de dados, trabalhando com
# imagens, criando apps, etc... sem precisar escrever
# todo o código do zero e usando funções e classes
# das bibliotecas para criar programas, scripts, etc. 
import os
# Importando biblioteca os para manipular
# o sistema operacional via terminal

# Usando o comando cls no terminal
os.system('cls')

# Conectar com base de dados mydatabase.db
conexao = sqlite3.connect('mydatabase.db')
print('Conexão com banco de dados criada com sucesso!')

# Criar um cursor para manipular o banco de dados
cursor = conexao.cursor()

# Pedir o nome da tabela ao usuário
nome_tabela = ''
while True:
    # O input por padrão recebe um dado str
    nome_tabela = input('Informe o nome da tabela: ') 

    # Verificar se o usuário informou um nome váido
    if nome_tabela != '' and len(nome_tabela) > 3:
        print(f'Nome {nome_tabela} para tabela é válido.')
        break
    else:
        print('Infome um nome válido para a tabela!')

# Criar uma tabela usando python com sqlite
# O f antes da string permite que sejam inseridas
# variáveis dentro de {} ao longo da string 
# O execute permite que sejam executados comandos SQL
cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        email TEXT
    )
''')

print('Tabela criada com sucesso.\n')

# Pedir os dados da tabela ao usuário usando laço while
usuario_nome = ''
usuario_idade = 0
usuario_email = ''
while True:
    # Ler dados
    usuario_nome = input('Informe o nome do usuário: ') 
    usuario_idade = input('Informe a idade do usuário: ') 
    usuario_email = input('Informe o e-mail do usuário: ') 

    # Converter idade para int
    usuario_idade = int(usuario_idade)

    # Validar dados com variáveis que tem valor True ou False
    # Em python em vez de && usamos and
    validacao_1 = usuario_nome != '' and len(usuario_nome) > 3
    # Validar idade
    validacao_2 = usuario_idade > 10 and usuario_idade < 100
    # A palavra reservada in verifica se um valor está "em" uma variável
    validacao_3 = '@' in usuario_email and len(usuario_email) > 5

    # O if pode verificar se um valor é True sem usar == 
    if validacao_1 and validacao_2 and validacao_3:
        print(f'Nome {usuario_nome}, idade {usuario_idade}, e {usuario_email} são válidos.')
        break
    # Mensagem de erro de input de dados
    else:
        print(f'Nome é válido: {validacao_1}')
        print(f'Idade é válida: {validacao_2}')
        print(f'E-mail é válido: {validacao_3}')
        print('Infome dados válidos!')

print('\nDados válidos inseridos!')

# Inserir dados na tabela criada anteriormente
cursor.execute(f'''
    INSERT INTO {nome_tabela} (nome, idade, email)
    VALUES ('{usuario_nome}', {usuario_idade}, '{usuario_email}')
''')

# Comitar/Executar mudanças para a base de dados
conexao.commit()
print('Dados inseridos com sucesso!')

# Importante: Fechar a conexão com a base de dados
conexao.close()
print('Conexão com base de dados fechada com sucesso.')
