import os
import sqlite3
from datetime import datetime


class LogicaBanco:
    def criar_conexao(self, nome_base):
        try:
            conn = sqlite3.connect(nome_base)
            print('Conexão estabelecida!')
            return conn
        except Exception as e:
            print(f'Erro: {str(e)}')


    def criar_tabela(self, nome_tabela):
        try:
            conn = self.criar_conexao('base.db')
            cursor = conn.cursor()

            sql_string = f"""
            create table if not exists {nome_tabela} (
                id integer primary key,
                registro text(150),
                data_hora_registrado text(50)
            )
            """

            cursor.execute(sql_string)
            cursor.close()
            conn.commit()
            conn.close()
            print(f'Tabela {nome_tabela} criada com sucesso!')
        except Exception as e:
            print(f'Erro: {str(e)}')


    def insere_registro(self, nome_tabela, registro):
        try:
            conn = self.criar_conexao('base.db')
            cursor = conn.cursor()

            sql_string = f"""
                insert into {nome_tabela} (registro, data_hora_registrado)
                values ('{registro}', '{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}')
            """

            cursor.execute(sql_string)
            cursor.close()
            conn.commit()
            conn.close()
            print(f'Dados inseridos em {nome_tabela} com sucesso!')
        except Exception as e:
            print(f'Erro: {str(e)}')


    def selecionar_ultimo_registro_inserido(self, nome_tabela):
        try:
            
            # trazer o ultimo registro via id
            # pelo maior id
            # adicionar como opcao no main em review.py

            ...
        except Exception as e:
            print(f'Erro: {str(e)}')
    

    def deletar_registro(self, id_linha, nome_tabela):
        try:

            # deletar registro via id
            # adicionar como opcao no main em review.py

            ...
        except Exception as e:
            print(f'Erro: {str(e)}')


    def selecionar_quantidade_registros(self, nome_tabela):
        try:
            # usar select para mostrar quantidade de registros
            # adicionar como opcao no main em review.py
            ...
        except Exception as e:
            print(f'Erro: {str(e)}')


if __name__ == '__main__':
    os.system('cls')
    objeto_banco = LogicaBanco()
    objeto_banco.criar_tabela('registros')
    objeto_banco.insere_registro(nome_tabela='registros', registro='testando 2')