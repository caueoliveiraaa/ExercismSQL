# realizando importações de bibliotecas
# por padrão, elas serão importadas no começo
# dos arquivos/programas .py
import os
import time

# .system server para enviar comandos para o terminal
# entre outras funções ...
os.system('cls')
# os.system('dir')

# o taskkill server para parar o arquivo executável
# responsável por rodar uma aplicação ou sistema
# os.system('taskkill /f /im chrome.exe')

# suicidio cmd
# os.system('taskkill /f /im cmd.exe')
os.system('python --version')

# tipos de dados em python
numero_inteiro_1: int = 5
numero_inteiro_2: int = 5500
numero_inteiro_3: int = 100
print(f'\nDados das variáveis do tipo int: {numero_inteiro_1}, {numero_inteiro_2}, {numero_inteiro_3}')

nome: str = 'Cauê'
sobrenome: str = 'Oliveira'
texto_aleatorio: str = 'Hahahahha'
print(f'\nDados das variáveis do tipo str: {nome}, {sobrenome}, {texto_aleatorio}')

salario_dev: float = 1.545
nota_aluno: float = 7.5
temperatura: float = 35.9
print(f'\nDados das variáveis do tipo float: {salario_dev}, {nota_aluno}, {temperatura}')
print(f'\nArredondando a variável salario_dev: {round(salario_dev, 2)}')

eh_verdade: bool = True
eh_mentira: bool = False
numero_1_eh_maior_que_numero_2: bool = numero_inteiro_1 > numero_inteiro_2
print(f'\nDados das variáveis do tipo bool: {eh_verdade}, {eh_mentira}, {numero_1_eh_maior_que_numero_2}')

# Criando uma lista com os dados das variáveis
lista_de_dados: list = [
    numero_inteiro_1,  # 0
    numero_inteiro_2,  # 1
    numero_inteiro_3,  # 2
    nome,              # 3
    sobrenome,         # ...
    texto_aleatorio,
    salario_dev,
    nota_aluno,
    temperatura,
    eh_verdade,
    eh_mentira,
    numero_1_eh_maior_que_numero_2
]

print(f'\nMostrando o dado da posição 0: {lista_de_dados[0]}')
print(f'\nMostrando o dado da posição 3: {lista_de_dados[3]}')
print(f'\nMostrando o dado da posição 7: {lista_de_dados[7]}')

print('esperando...')
time.sleep(5)
os.system('cls')

for item in lista_de_dados: 
    print(item)