import os
import sqlite3


class LogicaBanco:
    def criar_conexao(self, nome_base):
        try:
            ...
        except Exception as e:
            print(f'Erro: {str(e)}')


    def criar_tabela(self, nome_tabela):
        try:
            ...
        except Exception as e:
            print(f'Erro: {str(e)}')


    def insere_registro(self, nome_tabela):
        try:
            ...
        except Exception as e:
            print(f'Erro: {str(e)}')


    def retorna_ultimo_registro_inserido(self, nome_tabela):
        try:
            ...
        except Exception as e:
            print(f'Erro: {str(e)}')
    

    def deletar_registro(self, id_linha, nome_tabela):
        try:
            ...
        except Exception as e:
            print(f'Erro: {str(e)}')


    def retornar_quantidade_registros(self, nome_tabela):
        try:
            ...
        except Exception as e:
            print(f'Erro: {str(e)}')


if __name__ == '__main__':
    os.system('cls')