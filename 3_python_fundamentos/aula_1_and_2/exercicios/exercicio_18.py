# Exercício 18:
# Crie um programa que solicite ao usuário que insira a
#  quantidade de notas do aluno a serem calculadas.
# Em seguida, peça para o usuário digitar as notas uma por uma.
#  Armazene essas notas em uma lista.
# Calcule a média das notas utilizando um for loop para somar todos os
#  elementos da lista e dividir pela quantidade de notas.
# Verifique se a média é maior ou igual a 6.0. Se a média for maior
#  ou igual a 6.0, exiba a mensagem "Aluno Aprovado!".
# Caso contrário, exiba a mensagem "Aluno Reprovado!".
import os

def ler_quantidade_notas():
    while True:
        try:
            quantidade_notas = int(input('Informe a quantidade de notas: '))

            if quantidade_notas > 0:
                return quantidade_notas
            else:
                raise ValueError('Informe números acima de zero!')

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            print('Informe uma quantidade válida!')

def ler_notas(quantidade_notas):    
    lista_notas = []
    
    while len(lista_notas) < quantidade_notas:
        try:
            nota = float(input(f'Informe a {len(lista_notas) + 1}º uma nota: '))

            if nota >= 0 and nota <= 10:
                lista_notas.append(nota)

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            print('Informe uma nota válida!')

    return lista_notas

def calcula_media(lista_notas):
    soma = 0
    for nota in lista_notas:
        soma += nota

    return soma / len(lista_notas)

def verificar_media(media):
    if media >= 6:
        print(f'O aluno foi aprovado com média {media}!')
    else:
        print(f'O aluno foi reporvado com média {media}!')

def script():
    os.system('cls')
    quantidade_notas = ler_quantidade_notas()
    lista_notas = ler_notas(quantidade_notas)
    print(f'Notas: {lista_notas}')
    media = calcula_media(lista_notas)
    verificar_media(media)
    
if __name__ == '__main__':
    script()