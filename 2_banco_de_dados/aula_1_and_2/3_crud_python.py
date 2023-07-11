import sqlite3
import os

os.system('cls')
conexao = sqlite3.connect('mydatabase.db')
print('Conexão criada com sucesso.')
cursor = conexao.cursor()

# Mensagem para CRUD
menu_crud = '\nEscolha uma operação abaixo: '
menu_crud += '\n1 - Selecionar'
menu_crud += '\n2 - Deletar'
menu_crud += '\n3 - Atualizar'
menu_crud += '\n4 - Inserir'
menu_crud += '\n5 - Sair'
menu_crud += '\nInforme a opção: '

# While que rodará o programa
while True:
    # Ler a opção do usuário 
    operacao = input(menu_crud)
    
    # Verificar a operação informada
    if operacao == '1':
        os.system('cls')

        # Executar o código SQL
        cursor.execute(f'''
            SELECT * FROM usuarios
        ''')

        # Extrair o resultado que voltou do banco de dados
        # através do SELECT que selecionou os dados para o programa
        resultados = cursor.fetchall()
        for item in resultados:
            print(item)

    elif operacao == '2':
        # Ler id da coluna a deletar

        # Executar o código SQL

        # Printar mensagem de sucesso para quando deletar

        ...

    elif operacao == '3':
        # Ler o id da coluna a modificar

        # Executar o código SQL

        # Printar mensagem de sucesso para quando deletar
        ...

    elif operacao == '4':
        # Ler os dados novos

        # Validar os dados

        # Se válidos, vamos inserir na base de dados

        # Senão, mostrar mensagem de erro ao usuário

        ...
    elif operacao == '5':
        print('Laço de repetição parado com sucesso!')
        break





# Compactar nossas mudanças, para então enviar elas ao banco de dados
conexao.commit()
print('Comitou dados com sucesso!')
# Fechar a conexão com a base de dados
conexao.close()
print('Conexão fechada com sucesso!')