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
    def delete_linha(id_linha):
        pass

        # DELETAR LINHA VIA ID

    @staticmethod
    def mostra_tabela(nome_tabela):
        pass

        ### EXTRAIR DADOS DA TABELA

        ### MOSTRAT DADOS COM UM FOR

    @staticmethod
    def atualiza_linha(id_linha, nome_novo, numero_novo, email_novo):
        pass

        ### USAR UPDATE PARA ATUALIZAR VIA ID


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

                #### VERFICAR DADOS COM IFS

                BancoDeDados.insere_dados(
                    nome_tabela=tabela,
                    nome_usuario=nome,
                    numero_usuario=numero,
                    email_usuario=email
                )
            elif operacao == 3:

                #### CRIAR LOGICA

                pass
            elif operacao == 4:

                #### CRIAR LOGICA

                pass
            elif operacao == 5:

                #### CRIAR LOGICA

                pass
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
    