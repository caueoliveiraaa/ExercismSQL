import os

 ####################### TOPO DO CODIGO ############################

def eh_positivo(numero_parametro):
    if numero_parametro > 0:
        return True
    else:
        return False


def sao_numeros_iguais(numero_parametro_1, numero_parametro_2):
    if eh_positivo(numero_parametro_1) and eh_positivo(numero_parametro_2):
        if numero_parametro_1 == numero_parametro_2:
            return True
        else:
            return False
    else:
        print('Informar apenas números positivos!')


# funcao para verificar e retornar qual numero de dois numeros eh o maior
# se ambos forem numeros positivos
def funcao():
    ...



# funcao para verificar qual numero de dois numeros eh menor
# se ambos forem numeros positivos
def funcao():
    ...









####################### PARTE INFERIOR #####################

def main():
    menu = f'''
    \nSelecione a função:
    0 - Sair
    1 - eh_positivo
    2 - sao_numeros_iguais
    3 - 
    4 -
    5 -
    6 -
    --> opcao: '''

    while True:
        try:
            funcao_selecionada = int(input(menu))

            if funcao_selecionada == 0:
                print('O programa encerrou')
                break

            elif funcao_selecionada == 1:
                numero = int(input('Informe um número: '))

                if eh_positivo(numero) is True:
                    print(f'O número {numero} é positivo')
                else:
                    print(f'O número {numero} é negativo')

            elif funcao_selecionada == 2:
                numero_1 = int(input('Informe o primeiro número: '))
                numero_2 = int(input('Informe o segundo número: '))

                if sao_numeros_iguais(numero_1, numero_2) is True:
                    print(f'O número {numero_1} é igual ao número {numero_2}')
                else:
                    print(f'O número {numero_1} é diferente do número {numero_2}')

            elif funcao_selecionada == 3:

                ...

            elif funcao_selecionada == 4:

                ...


        except Exception as e:
            print(f'Erro: {e}')    


if __name__== '__main__':
    os.system('cls') 
    main()