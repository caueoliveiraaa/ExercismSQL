# Exercício 3:
# Crie uma função que peça ao usuário que digite um número inteiro e, em seguida,
# armazene esse valor em uma variável. Crie mais funções para o usuário também informar 
# dados do tipo float e string, e armazene todos os dados em variáveis. Em seguida
# adicione todos esses items em uma lista e mostre os item através de um laço de repetição for. 
import os


def leia_inteiros():
    inteiro = 0
    while True:
        try:
            inteiro = int(input('Informe um número inteiro: '))
            break
        except:
            print('Informe um número inteiro válido!')
    
    return inteiro


def leia_strings():
    string = input('Informe uma string: ')
    return string


def leia_float():
    variavel_float = 0.0
    while True:
        try:
            variavel_float = float(input('Informe um número float: '))
            break
        except:
            print('Informe um número float válido!')
    
    return variavel_float


if __name__ == '__main__':
    os.system('cls')
    inteiro = leia_inteiros()
    string = leia_strings()
    variavel_float = leia_float()

    lista_de_dados = [inteiro, string, variavel_float]
    for item in lista_de_dados:
        print(item)
