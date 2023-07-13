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
        id_linha = input('Informe o ID da coluna a deletar: ')             
        id_linha = int(id_linha)
        os.system('cls')

        cursor.execute(f'''
            DELETE FROM usuarios 
            WHERE id = {id_linha};
        ''')

        print(f'Linha {id_linha} excluída com sucesso!')

    elif operacao == '3':
        # Ler id da coluna a atualizar
        id_linha = input('Informe o ID da coluna a alterar: ')             
        
        os.system('cls')
        id_linha = int(id_linha)

        # Ler os dados novos
        nome_novo = input('Informe o novo nome do usuário: ')             
        email_novo = input('Informe o novo e-mail do usuário: ')             
        idade_nova = input('Informe a nova idade do usuário: ')             
        idade_nova = int(idade_nova)

        # Validar os dados e inserir os mesmos caso sejam válidos
        if len(nome_novo) > 3 and idade_nova > 0 and '@' in email_novo:
            cursor.execute(f"""
                UPDATE usuarios 
                SET nome = '{nome_novo}', idade = {idade_nova}, email = '{email_novo}' 
                WHERE id = {id_linha};
            """)
            
            print(f'Dados atualizados com sucesso em id = {id_linha}!')
        else:
            print('Informe dados válidos para serem atualizados!')

    elif operacao == '4':
        # Ler os dados novos
        nome_novo = input('Informe o nome do usuário: ')             
        email_novo = input('Informe o e-mail do usuário: ')             
        idade_nova = input('Informe a idade do usuário: ')             
        
        os.system('cls')
        idade_nova = int(idade_nova)

        # Validar os dados e inserir os mesmos caso sejam válidos
        if len(nome_novo) > 3 and idade_nova > 0 and '@' in email_novo:
            cursor.execute(f"""
                INSERT INTO usuarios (nome, idade, email)
                VALUES ('{nome_novo}', {idade_nova}, '{email_novo}');
            """)
            
            print(f'Dados {nome_novo}, {idade_nova}, e {email_novo} inseridos com sucesso!')
        else:
            print('Informe dados válidos para serem inseridos!')
    elif operacao == '5':
        print('Laço de repetição parado com sucesso!')
        break





# Compactar nossas mudanças, para então enviar elas ao banco de dados
conexao.commit()
print('Comitou dados com sucesso!')
# Fechar a conexão com a base de dados
conexao.close()
print('Conexão fechada com sucesso!')