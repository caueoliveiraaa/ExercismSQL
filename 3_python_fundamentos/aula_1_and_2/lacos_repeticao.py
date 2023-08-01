import os
from operadores import verifica_idade
from operadores import verifica_numeros


def script_idade():
    while True:
        # rodar funcao da idade
        verifica_idade()

        # verificar se deve continuar
        verificao = input('Informe s para sair, e qualquer outro char para continuar: ')

        # deixar letras minusculas
        verificao = verificao.lower()

        # parar loop
        if verificao == 's':
            print('Programa parou!')
            break


def script_numeros(limite_loop):
    contador = 0
    while contador < limite_loop:
        os.system('cls')
        contador += 1
        verifica_numeros()
    
    print(f'O loop rodou {limite_loop} vezes!')


if __name__ == '__main__':
    os.system('cls')
    # script_idade()
    limite_loop = int(input('Informe quantas vezes o programa deve rodar: '))
    script_numeros(limite_loop)

