# Escrever uma função que solicita ao usuário uma senha e verifica se ela atende a alguns critérios de segurança.
# Usar laço de repetição para rodar até uma senha válida ser informada e a mesma ser informada duas vezes de
# forma identica para confirmação da senha.
# Critérios de segurança:
# A senha deve conter pelo menos 8 caracteres.
# A senha deve conter pelo menos uma letra maiúscula e uma letra minúscula.
# A senha deve conter pelo menos um número.

import os

lista_letras_minusculas = [
    'a', 'b', 'c', 'd', 'e', 'f'
    'g', 'h', 'i', 'j' 'k', 'l', 'm'
    'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

lista_letras_maiusculas = [
    'A', 'B', 'C', 'D', 'E', 'F'
    'G', 'H', 'I', 'J' 'K', 'L', 'M'
    'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z'
]

numeros = [
    '0', '1', '2',
    '3', '4', '5',
    '6', '7', '8',
    '9'
]


def receber_senha_valida():
    senha_valida = False
    while senha_valida is False:
        senha_temporaria = input('Informe a senha: ')

        # variaveis para validar senha
        validou_characteres = False
        validou_letras = False
        validou_numero = False
        
        # valida tamanho da senha
        if len(senha_temporaria) >= 8:
            validou_characteres = True
        
        # variaveis para validar minusculas / maiusculas
        minuscula_apareceu = False
        maiuscula_apareceu = False

        # transforma senha em lista
        lista_chars = list(senha_temporaria)

        # verifica se cada letra da senha
        # aparece nas listas de letras
        # minusculas e maiusculas
        for letra in lista_chars:
            if letra in lista_letras_minusculas:
                minuscula_apareceu = True
            elif letra in lista_letras_maiusculas:
                maiuscula_apareceu = True

        # verifica se achou tanto uma maiuscula
        # quanto uma minuscula
        if maiuscula_apareceu is True and minuscula_apareceu is True:
            validou_letras = True

        # verifica se aparece numero na senha
        for char in lista_chars:
            if char in numeros:
                validou_numero = True
                break

        if validou_numero is True and validou_letras is True and validou_characteres is True:
            # pedir e validar segunda senha
            senha_nova = input('Informe a senha mais uma vez: ')

            # validar senhas
            estrelinha = '*'
            if senha_nova == senha_temporaria:
                print(f'Senha {estrelinha * len(senha_nova)} criada com sucesso!')
                senha_valida = True
            else:
                print('As senhas não batem! Tente outra vez!')
        else:
            print(f'Tem pelo menos 8 characteres: {validou_characteres}')
            print(f'Tem tanto letra minuscula como maiuscula: {validou_letras}')
            print(f'Tem pelo menos um numero: {validou_numero}')


if __name__ == '__main__':
    os.system('cls')
    receber_senha_valida()