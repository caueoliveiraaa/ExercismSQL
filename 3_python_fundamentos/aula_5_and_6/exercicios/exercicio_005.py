# 5 - Crie uma classe Alimento com atributos como nome e calorias. Crie subclasses Fruta, Legume
# e Carne que herdam de Alimento e implementam seus próprios atributos. Crie uma função que aceita 
# uma lista de alimentos e calcula o total de calorias usando polimorfismo. Para mais precisão no
# exercício, é ideal pesquisar as calorias dos alimentos e criar objetos das subclasses com seus 
# respectivos construtores e atributos.
from abc import ABC, abstractmethod

import pyautogui

class Alimento(ABC):
    def __init__(self, calorias, nome):
        self.calorias = calorias
        self.nome = nome

class Fruta(Alimento):
    pass

class Carne(Alimento):
    pass

class Legume(Alimento):
    pass


def calcula_calorias(lista_calorias):
    soma_calorias = 0
    for caloria in lista_calorias:
        soma_calorias += caloria
    
    return soma_calorias

cenoura = Legume(5, 'cenoura')
vagem = Legume(10, 'vagem')
beterraba = Legume(20, 'beterraba')

lista_legumes = [
    cenoura.calorias,
    vagem.calorias,
    beterraba.calorias
]

calorias_total_legumes = calcula_calorias(lista_legumes)
print(f'A soma de calorias de {cenoura.nome}, ', end=' ') 
print(f'{vagem.nome}, e {beterraba.nome}', end=' ')
print(f'é: {calorias_total_legumes}')

frango = Carne(100, 'Filé de frango')
bife = Carne(150, 'Patinho')
picanha = Carne(200, 'Picanha')

lista_carnes = [
    frango.calorias,
    bife.calorias,
    picanha.calorias
]

calorias_total_carnes = calcula_calorias(lista_carnes)
print(f'A soma de calorias de {frango.nome}, ', end=' ') 
print(f'{bife.nome}, e {picanha.nome}', end=' ')
print(f'é: {calorias_total_carnes}')

banana = Fruta(50, 'Banana')
melancia = Fruta(20, 'Melância')
maracuja = Fruta(60, 'Passion Fruit')

lista_frutas = [    
    banana.calorias,
    melancia.calorias,
    maracuja.calorias
]

calorias_total_frutas = calcula_calorias(lista_frutas)
print(f'A soma de calorias de {banana.nome}, ', end=' ') 
print(f'{melancia.nome}, e {maracuja.nome}', end=' ')
print(f'é: {calorias_total_frutas}')