# No começo do arquivo realizamos as importações necessárias
# Biblioteca sqlite que serve para manipular bancos de dados do sqlite
import sqlite3
# Biblioteca os que server para manipular o sistema operacional
import os

os.system('cls')

# Conexão com o banco de dados
conexao = sqlite3.connect('mydatabase.db')
print('Conexão criada com sucesso.')

# Cursor para manipular o banco de dados
cursor = conexao.cursor()

# Variável para criar a nova tabela
nome_tabela = ''

# OBS: o True e False (valores booloan),
# começam com letra maiúscula em Python
while True:
    # Lero o nome da tabela informado pelo usuário
    nome_tabela = input('Informe o nome da tabela: ')

    # Verificar se o nome é válido
    if nome_tabela != '' and len(nome_tabela) > 3:
        print(f'Nome {nome_tabela} é válido para tabela!')
        break
    else:
        print('Informe um nome válido!')

# Executar comandos SQL no banco de dados
# com a função execute da biblioteca sqlite
cursor.execute(f'''

    CREATE TABLE IF NOT EXISTS {nome_tabela} (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER,
        email TEXT
    )

''')

print('Tabela criada com sucesso!\n')

# Pedir os dados ao usuário
# para preencher a tabela
usuario_nome = ''
usuario_idade = 0
usuario_email = ''

while True:
    # Ler dados
    # OBS: input por padrão recebe strings/textos
    usuario_nome = input('Informe o nome do usuário: ')
    usuario_idade = input('Informe a idade do usuário: ')
    usuario_email = input('Informe o e-mail do usuário: ')

    # Converter idade para inteiro
    usuario_idade = int(usuario_idade)

    # Validar os dados armazenando valores True ou False
    # em variáveis de validação

    validacao_1 = usuario_nome != '' and len(usuario_nome) >= 3
    validacao_2 = usuario_idade > 10 and usuario_idade < 100
    validacao_3 = usuario_email != '' and '@' in usuario_email

    if validacao_1 and validacao_2 and validacao_3:
        print(f'Nome {usuario_nome}, idade {usuario_idade}, e-mail {usuario_email} são dados válidos!')
        break
    else:
        print(f'Nome é válido: {validacao_1}')
        print(f'Idade é válida: {validacao_2}')
        print(f'E-mail é válido: {validacao_3}')
        print('Informes dados válidos!')


# Inserir os dados na nossa base de dados
cursor.execute(f'''

    INSERT INTO {nome_tabela} (nome, idade, email)
    VALUES ('{usuario_nome}', {usuario_idade}, '{usuario_email}')

''')

print('Dados inseridos com sucesso!')

# Compactar nossas mudanças, para então enviar elas ao banco de dados
conexao.commit()
print('Comitou dados com sucesso!')
# Fechar a conexão com a base de dados
conexao.close()
print('Conexão fechada com sucesso!')