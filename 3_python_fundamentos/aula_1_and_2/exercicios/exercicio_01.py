# Exercício 1:
# Escreva uma função que solicite ao usuário que insira seu nome e, em seguida,
# armazene esse valor em uma variável. Em seguida, exiba uma mensagem de boas-vindas
# usando o nome digitado.

import os 


def boas_vindas_usuario():
    nome = input('Informe o seu nome: ')
    print(f'Bem vindo a empresa, {nome}')


if __name__ == '__main__':
    os.system('cls')
    boas_vindas_usuario()