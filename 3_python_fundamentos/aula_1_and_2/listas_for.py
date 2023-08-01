import os


def mostrar_lista():
    lista_dados = [
        1, # 0
        2, # 1
        3, # 2
        'hello', # 3
        'hi', # 4
        False, # 5 
        True, # 6
        1.5, # 7 
        20, # 8
        'Texto !!'
    ]

    for item in lista_dados:
        print(item)


def obter_mostrar_dados():
    lista_input = []
    for i in range(5):
        item = input(f'Informe o {i + 1}º item: ')
        lista_input.append(item)
    
    print('\nItens informados pelo usuário: ')
    for item in lista_input:
        print(item)


def script_lista():
    lista_dados = []
    contador = 0

    # receber 10 itens do usuario
    while contador < 10:
        contador += 1
        item_informado = input(f'Informe o {contador}º item: ')
        lista_dados.append(item_informado)

    # mostrar os itens recebidos
    # acessando tambem os indices / posicoes
    for indice, item in enumerate(lista_dados):
        print(f'Posição {indice} - Valor {item}')


    # loop para o usuário acessar
    # itens especificos da lista
    while True:
        try:
            posicao_item = int(input('Informe a posição do item desejado: '))
            print(f'O item que está na posição {posicao_item} é: {lista_dados[posicao_item]}')

            verificao = input('Informe s para parar, informe outro valor para continuar: ')
            if verificao == 's':
                print('Programa parou')
                break
        except:
            print('Informe apenas inteiros para posições em listas!!!')


if __name__ == '__main__':
    os.system('cls')
    # mostrar_lista()
    # obter_mostrar_dados()   
    script_lista()



