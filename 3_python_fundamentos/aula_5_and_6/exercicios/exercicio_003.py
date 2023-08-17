# 3 - Crie uma classe base Veiculo com atributos como marca, modelo e métodos como ligar()
# e desligar(), entre outros. Crie as subclasses Carro e Moto que herdam de Veiculo e
# implementam seus próprios métodos beaseando-se na abstratação de Veiculo. Em seguida,
# crie uma classe Garagem que aceita veículos e gerencia o estacionamento usando herança.
# Crie e trabalhe com os getters e setters para a classe Garagem.
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo, ligado):
        self.marca = marca
        self.modelo = modelo
        self.ligado = ligado

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class Carro(Veiculo):
    def ligar(self):
        if self.ligado == True:
            print('O carro já está ligado!')
        else:
            self.ligado = True
            print('Carro ligado com sucesso.')

    def desligar(self):
        if self.ligado == False:
            print('O carro já está desligado!')
        else:
            self.ligado = False
            print('Carro desligado com sucesso.')


class Moto(Veiculo):
    def ligar(self):
        if self.ligado == True:
            print('A moto já está ligada!')
        else:
            self.ligado = True
            print('Moto ligada com sucesso.')

    def desligar(self):
        if self.ligado == False:
            print('A moto já está desligada!')
        else:
            self.ligado = False
            print('Moto desligada com sucesso.')


class Garagem:
    def __init__(self):
        self.veiculos_estacionados = []

    def estacionar(self, auto_nome):
        self.veiculos_estacionados.append(auto_nome)
        print(f'Veículo {auto_nome} estacionado com sucesso.')

    def mostra_autos_estacionados(self):
        if len(self.veiculos_estacionados) > 0:
            print('GARAGEM:')
            for indice, veiculo in enumerate(self.veiculos_estacionados):
                print(f'Veículo {indice + 1}: {veiculo}')
        else:
            print('Ainda não existem veículos na garagem!')


moto_objeto = Moto('Honda', 'Hornert', False)
carro_objeto = Carro('Fiat', 'Palio', False)

print(moto_objeto.marca)
print(moto_objeto.modelo)
moto_objeto.desligar()
moto_objeto.ligar()
moto_objeto.desligar()

print('\n')

print(carro_objeto.marca)
print(carro_objeto.modelo)
carro_objeto.desligar()
carro_objeto.ligar()
carro_objeto.desligar()

print('\n')

garagem_objeto = Garagem()
garagem_objeto.mostra_autos_estacionados()

garagem_objeto.estacionar(f'Carro da mãe - {carro_objeto.marca}')
garagem_objeto.estacionar(f'Carro do pai - {carro_objeto.marca}')
garagem_objeto.estacionar(f'Moto de casa - {moto_objeto.marca}')
garagem_objeto.estacionar(f'Moto da empresa - {moto_objeto.modelo}')

print('\n')

garagem_objeto.mostra_autos_estacionados()

