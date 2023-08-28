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
def retorna_maior_numero(numero_parametro_1, numero_parametro_2):
    numero_maior = None

    if eh_positivo(numero_parametro_1) and eh_positivo(numero_parametro_2):
        if numero_parametro_1 > numero_parametro_2:
            numero_maior = numero_parametro_1
        elif numero_parametro_1 < numero_parametro_2:
            numero_maior = numero_parametro_2
        else:
            print('Os números são iguais! Informe números diferentes!')
    else:
        print('Informar apenas números positivos!')

    return numero_maior


# funcao para verificar qual numero de dois numeros eh menor
# se ambos forem numeros positivos
def retorna_menor_numero(numero_parametro_1, numero_parametro_2):

    ...


# funcao para verificar se um numero eh impar ou par
# se ambos forem numeros positivos
def verifica_se_eh_impar_ou_par(numero_parametro):
    
    ...






####################### PARTE INFERIOR #####################

def main():
    menu = f'''
    \nSelecione a função:
    0 - Sair
    1 - eh_positivo
    2 - sao_numeros_iguais
    3 - retorna_maior_numero
    4 - retorna_menor_numero
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

                if eh_positivo(numero) == True:
                    print(f'O número {numero} é positivo')
                else:
                    print(f'O número {numero} é negativo')

            elif funcao_selecionada == 2:
                numero_1 = int(input('Informe o primeiro número: '))
                numero_2 = int(input('Informe o segundo número: '))

                if sao_numeros_iguais(numero_1, numero_2) == True:
                    print(f'O número {numero_1} é igual ao número {numero_2}')
                else:
                    print(f'O número {numero_1} é diferente do número {numero_2}')

            elif funcao_selecionada == 3:
                numero_1 = int(input('Informe o primeiro número: '))
                numero_2 = int(input('Informe o segundo número: '))
                
                numero_retornado = retorna_maior_numero(numero_1, numero_2)
                if numero_retornado != None:
                    print(f'O maior número é: {numero_retornado}')


            elif funcao_selecionada == 4:

                ...


        except Exception as e:
            print(f'Erro: {e}')    


if __name__== '__main__':
    os.system('cls') 
    main()