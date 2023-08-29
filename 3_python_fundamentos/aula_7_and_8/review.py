import os


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


def retorna_menor_numero(numero_parametro_1, numero_parametro_2):
    numero_menor = None

    if eh_positivo(numero_parametro_1) and eh_positivo(numero_parametro_2):
        if numero_parametro_1 < numero_parametro_2:
            numero_menor = numero_parametro_1
        elif numero_parametro_1 > numero_parametro_2:
            numero_menor = numero_parametro_2
        else:
            print('Os números são iguais! Informe números diferentes!')
    else:
        print('Informar apenas números positivos!')

    return numero_menor


def verifica_se_eh_impar_ou_par(numero_parametro):
    resultado = ''

    if eh_positivo(numero_parametro):
        if numero_parametro % 2 == 0:
            resultado = 'par'
        else:
            resultado = 'ímpar'
    else:
        print('Informar apenas números positivos!')

    return resultado    


def retorna_maior_numero_em_lista(lista_de_dados):
    maior_numero = lista_de_dados[0]

    for item in lista_de_dados:
        if item > maior_numero:
            maior_numero = item

    return maior_numero


def retorna_menor_numero_em_lista(lista_de_dados):
    maior_numero = lista_de_dados[0]

    for item in lista_de_dados:
        if item < maior_numero:
            maior_numero = item

    return maior_numero


def retorna_quantidade_de_impares_e_pares_em_lista(lista_de_dados):
    contador_impares = 0
    contador_pares = 0

    for item in lista_de_dados:
        if item % 2 == 0:
            contador_pares += 1
        else:
            contador_impares += 1

    return contador_pares, contador_impares


def rodar_calculadora(numero_1, numero_2, operacao):
    if operacao == 1:
        return numero_1 + numero_2
    elif operacao == 2:
        return numero_1 - numero_2
    elif operacao == 3:
        return numero_1 * numero_2
    elif operacao == 4:
        return numero_1 / numero_2


# funcao para verificar quantas vezes uma letra especificada pelo usuario aparece 
# dentro de um texto tambem informado pelo usuario e mostre quantas vezes 
# numeros de 1 a 9 aparecem caso tenha numeros no texto
# a funcao deve tratar todo o texto com lowercase " .lower() "
def funcao():
    ...



# funcao para verificar quanto um funcionario ganhou durante um mes,
# com base no valor que o colaborador ganha por hora e em quantos dias
# aquele mes atual tem. Passar tbm a quantidade de horas trabalhadas por dia
# Todas essas informacoes devem ser passadas por parametro
def funcao():
    ...


# funcao para verificar quantos items existem em uma lista no total,
#  mas também a quantidade de itens que sao string ou ints ou floats dentro da lista.
# A função deve retornar a quantidade de cada um. Quando os dados forem enviados pelo
#  usuario via input, a lista precisa ter pelo menos 6 itens, dois send inteiros,
# dois sendo floats e dois sendo strings antes de chamar a funcao
def funcao():
    ...


def main():
    menu = f'''
    \nSelecione a função:
0 - Sair
1 - eh_positivo
2 - sao_numeros_iguais
3 - retorna_maior_numero
4 - retorna_menor_numero
5 - verifica_se_eh_impar_ou_par
6 - retorna_maior_numero_em_lista
7 - retorna_menor_numero_em_lista
8 - retorna_quantidade_de_impares_e_pares_em_lista
9 - rodar_calculadora
10 - 
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
                numero_1 = int(input('Informe o primeiro número: '))
                numero_2 = int(input('Informe o segundo número: '))
                
                numero_retornado = retorna_maior_numero(numero_1, numero_2)
                if numero_retornado != None:
                    print(f'O maiomenor número é: {numero_retornado}')

            elif funcao_selecionada == 5:
                numero = int(input('Informe um número: '))
                resultado = verifica_se_eh_impar_ou_par(numero)

                if resultado != '':
                    print(f'O número {numero} é {resultado}!')

            elif funcao_selecionada == 6:
                lista_de_dados = []
                contador = 0
                limite = int(input('Informe quantos items serão inseridos: '))

                while contador < limite:
                    try:
                        item = int(input(f'Informe o {contador + 1}º item: '))
                        lista_de_dados.append(item)
                        contador += 1
                    except:
                        print('Informe um número válido')

                maior_numero = retorna_maior_numero_em_lista(lista_de_dados)
                print(f'O maior número da lista é: {maior_numero}')

            elif funcao_selecionada == 7:
                lista_de_dados = []
                contador = 0
                limite = int(input('Informe quantos items serão inseridos: '))

                while contador < limite:
                    try:
                        item = int(input(f'Informe o {contador + 1}º item: '))
                        lista_de_dados.append(item)
                        contador += 1
                    except:
                        print('Informe um número válido')

                menor_numero = retorna_menor_numero_em_lista(lista_de_dados)
                print(f'O menor número da lista é: {maior_numero}')

            elif funcao_selecionada == 8:
                lista_de_dados = []
                contador = 0
                limite = int(input('Informe quantos items serão inseridos: '))

                while contador < limite:
                    try:
                        item = int(input(f'Informe o {contador + 1}º item: '))
                        lista_de_dados.append(item)
                        contador += 1
                    except:
                        print('Informe um número válido')

                qty_par, qty_impar = retorna_quantidade_de_impares_e_pares_em_lista(lista_de_dados)
                print(f'A quantidade de pares é {qty_par} e de ímpares é {qty_impar}')

            elif funcao_selecionada == 9:
                numero_1 = int(input('Informe o primeiro número: '))
                numero_2 = int(input('Informe o segundo número: '))

                menu_operacoes = ''' 
                \nOperações:
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
--> opcao: '''

                while True:
                    try:
                        operacao = int(input(menu_operacoes))
                        if operacao in [1, 2, 3, 4]:
                            resultado = rodar_calculadora(numero_1, numero_2, operacao)
                            print(f'O resultado da operação é: {resultado}')
                            break
                        else:
                            print('Informe uma operação válida!')
                    except:
                        print('Informe um número válido')

            elif funcao_selecionada == 10:

                ...

            elif funcao_selecionada == 11:

                ...

            elif funcao_selecionada == 12:
                
                ...

        except Exception as e:
            print(f'Erro: {e}')    


if __name__== '__main__':
    os.system('cls') 
    main()