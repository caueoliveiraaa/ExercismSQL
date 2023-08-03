# # Exercício 4:
# Desenvolva uma função que mostre na tela uma contagem
# regressiva de 5 a 1, com uma pausa de um segundo entre cada número.
import time

def contagem_regressiva_for():
    for numero in range(5, 0, -1):
        print(numero)
        time.sleep(1)


def contagem_regressiva_manual():
    contador = 5
    while contador > 0:
        print(contador)
        time.sleep(1)
        contador -= 1    


if __name__ == '__main__':
    contagem_regressiva_for()
    contagem_regressiva_manual()