import pyautogui as p

for i in range(10):
    if i % 2 == 0:
        print(f'{i} É par')
    else:
        print(f'{i} É ímpar')


let lista_de_numeros = [
    1,  # 0
    24, # 1
    35, # 2
    44, # 3
    59  # 4
]

soma_dos_pares = 0
soma_dos_impares = 0

for i in range(len(lista_de_numero)):
    if lista_de_numero[i] % 2 == 0:
        soma_dos_pares = soma_dos_pares + lista_de_numero[i]
    else:
        soma_dos_impares = soma_dos_impares + lista_de_numero[i]
