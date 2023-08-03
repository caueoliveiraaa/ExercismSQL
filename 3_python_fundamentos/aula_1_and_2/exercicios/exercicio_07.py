# Exercício 7:
# Crie uma função que pergunte ao usuário quais são seus três filmes
# favoritos e armazene cada filme em uma lista.
# Depois mostre esses items usando um for, com uma função distinta que
# recebe uma lista por parâmetro e mostra seus items. 

import os


def le_filmes_favoritos():
    lista_filmes = []
    while len(lista_filmes) < 3:
        try:
            filme_informado = input(f'Informe o {len(lista_filmes) + 1}º filme: ')
            if len(filme_informado) > 0:
                lista_filmes.append(filme_informado)
        except Exception as erro_ocorrido:
            print(f'Erro: {str(erro_ocorrido)}')

    return lista_filmes

def mostrar_lista_filmes(lista_filmes):
    for indice, nome_filme in enumerate(lista_filmes):
        print(f'{indice + 1}º filme: {nome_filme}')

def main():
    lista_filmes = le_filmes_favoritos()
    mostrar_lista_filmes(lista_filmes)

if __name__ == '__main__':
    os.system('cls')
    main()

