import os
import sqlite3
import pandas as pd 

# Instalar o pandas na nossa máquina local
# com o comando pip install pandas

def executar_comandos_sql(sql_string):
    """ Primeria docstring: Função para executar comandos SQL na base de dados usando pandas """

    # Criar conexão com a base de dados
    conexao = sqlite3.connect('mydatabase.db')

    # A função do pandas chamada read_sql_query executa SQL
    # e espera como parâmetros uma string com o SQL a ser executado
    # e a conexão com a base de dados
    retorno_do_sql = pd.read_sql_query(sql_string, conexao)

    # Fechar a conexão 
    conexao.close()

    # Retornar os dados do query (ou seja, da busca SQL)
    return retorno_do_sql


def mostrar_opcoes(colunas_lista):
    """ Função para mostrar as opções disponíveis do programa para o usuário """

    # Printar os dados usando um for na lista com as colunas disponíveis
    print('Colunas disponíveis:')
    for indice, coluna_string in enumerate(colunas_lista):
        print(f'Coluna {indice}: {coluna_string}')

    # O enumerate permite que seja possivel rodar o for com duas variáveis
    # uma sendo o indice (i) da linha, e a outra sendo o valor (dado/informação)

    print()


def retornar_media_coluna(coluna_nome):
    """ Função para retornar média de uma coluna informada pelo usuário """

    # Comando SQL
    sql_string = f'select avg({coluna_nome}) from usuarios'

    # Executar o SQL
    retorno = executar_comandos_sql(sql_string)

    # Mostrar o resultado
    print(f'Média da coluna {coluna_nome}: {retorno}')


def contar_linhas_coluna():
    """ Função para dar um COUNT na coluna informada pelo usuário """

    # Comando SQL

    # Executar o SQL


    # Mostrar o resultado


def buscar_palavras_em_colunas():
    """ Função para buscar partes específicas das palavras usando LIKE """

    # Criar a string com o padrão da palavra que será buscada

    # Comando SQL

    # Executar o SQL

    # Mostrar o resultado
    

def retornar_min_e_max_coluna():
    """ Função para mostrar o maior e o menor valor de uma coluna"""

    # Comando SQL

    # Executar o SQL

    # Mostrar o resultado


# START
os.system('cls')
retorno = executar_comandos_sql('select * from usuarios')
print(retorno)
mostrar_opcoes(['name', 'age', 'email'])