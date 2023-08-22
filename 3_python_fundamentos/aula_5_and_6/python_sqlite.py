import sqlite3
import os

# @staticmethod
# permite aceesar metodo sem criar objetos

class BancoDeDados:
    # Atributo PUBLICO da classe
    conexao = None

    @staticmethod  
    def criar_conexao(nome_base):
        BancoDeDados.conexao = sqlite3.connect(nome_base)
        print('Conexão estabelecida com sucesso.')
        return BancoDeDados.conexao


    @staticmethod
    def criar_tabela(nome_tabela_nova):
        cursor = BancoDeDados.conexao.cursor()

        sql_string = f''' 
            create table if not exists {nome_tabela_nova} (\
                id integer primary key,\
                nome text(40),\
                numero text(15),\
                email text(40)
            )
        '''

        cursor.execute(sql_string)
        cursor.close()
        print(f'Tabela {nome_tabela_nova} criada com sucesso.')


    @staticmethod
    def insere_dados(nome_tabela, nome_usuario, numero_usuario, email_usuario):
        cursor = BancoDeDados.conexao.cursor()

        sql_string = f"""
            insert into {nome_tabela}\
            (nome, numero, email)\
            values ('{nome_usuario}', '{numero_usuario}', '{email_usuario}')
        """

        cursor.execute(sql_string)
        BancoDeDados.conexao.commit()
        cursor.close()
        print(f'Dados: {nome_usuario} - {numero_usuario} - {email_usuario}', end=' ')
        print(f'inseridos em {nome_tabela} com sucesso.')

    @staticmethod
    def delete_linha(id_linha, nome_tabela):
        cursor = BancoDeDados.conexao.cursor()

        sql_query = f'''
            select * from {nome_tabela}
            where id = {id_linha}
        '''

        cursor.execute(sql_query)
        dados_banco = cursor.fetchall()

        if len(dados_banco) > 0:
            sql_delete = f'''
                delete from {nome_tabela}
                where id = {id_linha}
            '''

            cursor.execute(sql_delete)
            cursor.close()
            BancoDeDados.conexao.commit()
            print(f'Linha {id_linha} deletada com sucesso.')
        else:
            print(f'Tabela {nome_tabela} com id {id_linha} nao exite.')


    @staticmethod
    def mostra_tabela(nome_tabela):
        cursor = BancoDeDados.conexao.cursor()

        slq_query = f'''
            select * from {nome_tabela}
        '''

        cursor.execute(slq_query)
        dados_banco = cursor.fetchall()

        if len(dados_banco) > 0:
            print(f'\n\nDados da tabela {nome_tabela}:\n')
            for linha in dados_banco:
                for coluna in linha:
                    print(coluna, end=' ')
                print('\n')

            cursor.close()
        else:
            print(f'A tabela {nome_tabela} não possui registros.')


    @staticmethod
    def atualiza_linha(id_linha, nome_tabela, nome_novo, numero_novo, email_novo):
        cursor = BancoDeDados.conexao.cursor()

        sql_query = f'''
            select * from {nome_tabela}
            where id = {id_linha}
        '''

        cursor.execute(sql_query)
        dados_banco = cursor.fetchall()

        if len(dados_banco) > 0:
            sql_update = f"""
                update {nome_tabela}
                set nome = '{nome_novo}',
                numero = '{numero_novo}',
                email = '{email_novo}'
                where id = {id_linha}
            """

            cursor.execute(sql_update)
            cursor.close()
            BancoDeDados.conexao.commit()
            print(f'Linha {id_linha} atualizada com sucesso.')
        else:
            print(f'Tabela {nome_tabela} com id {id_linha} nao exite.')


    @staticmethod
    def valida_colunas_banco(nome, numero, email):
        # Validar email
        valida_email = False
        if len(email) >= 10 and '@' in email and '.' in email:
            valida_email = True

        
        # Validar nome    
        valida_nome = False
        numeros = [
            '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0'
        ]

        if len(nome) >= 3:
            valida_nome = True
            for numero in numeros:
                if numero in nome:
                    valida_nome = False
        
        # Validar nuemro
        valida_numero = False
        lista_simbilo = ['(', ')', '-', '+']
        if len(numero) >= 8 and len(numero) <= 14:
            numeros_lista = list(numero)

            contador = 0
            for n in numeros_lista:
                if n in numeros or n in lista_simbilo:
                    if n in numeros:
                        contador += 1
                elif n not in numeros and n not in lista_simbilo:
                    contador = 0
                    break
            
            if contador >= 8:
                valida_numero = True
       
        print(f'Nome é válido: {valida_nome}')
        print(f'Número é válido: {valida_numero}')
        print(f'E-mail é válido: {valida_email}')

        return valida_email and valida_nome and valida_numero


def database_manager():
    os.system('cls')
    conn = BancoDeDados.criar_conexao('base_de_dados.db')

    menu_interface = '''
1 - Criar tabela
2 - Inserir dados
3 - Deletar linha
4 - Mostrar tabela
5 - Aualizar linha
6 - Sair
Insira a operação (1 - 6): '''

    while True:
        try:
            operacao = int(
                input(menu_interface)
            )

            if operacao == 1:
                nome_tabela = input('Informe o nome da tabela nova: ')
                BancoDeDados.criar_tabela(nome_tabela)
            elif operacao == 2:
                tabela = input('Informe o nome da tabela: ')
                nome = input('Informe o nome do contato: ')
                numero = input('Informe o número do contato: ')
                email = input('Informe o e-mail do contato: ')

                dados_validos = BancoDeDados.valida_colunas_banco(
                    nome=nome,
                    numero=numero,
                    email=email
                )

                if dados_validos is True:
                    BancoDeDados.insere_dados(
                        nome_tabela=tabela,
                        nome_usuario=nome,
                        numero_usuario=numero,
                        email_usuario=email
                    )
                else:
                    print('Informe dados válidos!')
            elif operacao == 3:
                tabela = input('Informe o nome da tabela: ')
                id_linha = input('Informe o id da linha: ')
                
                BancoDeDados.delete_linha(
                    id_linha=id_linha, nome_tabela=tabela
                )   
            elif operacao == 4:
                tabela = input('Informe o nome da tabela: ')
                BancoDeDados.mostra_tabela(tabela)
            elif operacao == 5:
                tabela = input('Informe o nome da tabela a alterar: ')
                id_linha = input('Informe o id da linha a alterar: ')
                nome = input('Informe o novo nome do contato: ')
                numero = input('Informe o novo número do contato: ')
                email = input('Informe o nobo e-mail do contato: ')

                dados_validos = BancoDeDados.valida_colunas_banco(
                    nome=nome,
                    numero=numero,
                    email=email
                )

                if dados_validos:
                    BancoDeDados.atualiza_linha(
                        id_linha=id_linha,
                        nome_tabela=tabela,
                        nome_novo=nome,
                        numero_novo=numero,
                        email_novo=email
                    )
                else:
                    print('Informe dados válidos!')
            elif operacao == 6:
                print('Programa encerrado.')
                break
            else:
                print(
                    'Informe uma operação válida'
                )

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

    conn.close()
    print('Conexão encerrada.')


if __name__ == '__main__':
    database_manager()