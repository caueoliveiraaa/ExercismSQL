# Exercício 10:
# Crie uma função que converta um valor em horas para minutos e segundos.
# Solicite ao usuário que digite o valor em horas e, em seguida, exiba as conversões para minutos e segundos.
# Fórmula para converter horas em minutos: Minutos = Horas * 60
# Fórmula para converter horas em segundos: Segundos = Horas * 3600

import os 
import time

def ler_dados():
    while True:
        try:
            hora = int(input('Informe uma hora válida: '))
            return hora
        except:
            print('Dados inválidos!')

def converter_dados(hora):
    minutos = round(hora * 60, 2)
    segundos = round(hora * 3600, 2)
    return minutos, segundos

def exibir_dados(hora, minutos, segundos):
    print(f'\033[032mA hora {hora} convertida em minutos é: {minutos} \033[0m')
    print(f'\033[032mA hora {hora} convertida em segundos é: {segundos} \033[0m')

def script():
    hora = ler_dados()
    minutos, segundos = converter_dados(hora)
    exibir_dados(hora, minutos, segundos)

if __name__ == '__main__':
    os.system('cls')
    script()
