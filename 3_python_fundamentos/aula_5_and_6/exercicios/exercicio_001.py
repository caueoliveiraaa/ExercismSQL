# 1 - Crie uma classe abstrata chamada Animal com métodos falar(), comer() e mover().
# Crie subclasses Cachorro, Cavalo e Gato que herdam da classe Animal e implementam
# seus próprios métodos, printando frases diferentes.  
# Crie e trabalhe com os getters e setters para as subclasses.

from abc import ABC, abstractmethod

# CLASSE ABSTRATA (MODELO)
class Animal(ABC):
    def __init__(self, especie, idade, peso, cor):
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.cor = cor

    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def exibir_informacoes(self):
        pass


# SUBCLASSES
class Cavalo(Animal):
    def emitir_som(self):
        print('Prussxx.. EEeeeehehehehhe \U0001F434')

    def comer(self):
        print('Comendo capim \U0001F434')

    def mover(self):
        print('Pulando aleatoriamente \U0001F434')

    def exibir_informacoes(self):
        print(f'\nEspécie {self.especie}')
        print(f'Peso {self.peso}')
        print(f'Cor {self.cor}')
        print(f'Idade {self.idade}')

class Cachorro(Animal):
    def emitir_som(self):
        print('Au au \U0001F436')

    def comer(self):
        print('Comendo qualquer coisa \U0001F436')

    def mover(self):
        print('Correndo atrás do carteiro \U0001F436')

    def exibir_informacoes(self):
        print(f'\nEspécie {self.especie}')
        print(f'Peso {self.peso}')
        print(f'Cor {self.cor}')
        print(f'Idade {self.idade}')

class Gato(Animal):
    def emitir_som(self):
        print('Meaw meaw \U0001F63A')

    def comer(self):
        print('Comendo o sofá \U0001F63A')

    def mover(self):
        print('Pulando em todos os móveis \U0001F63A')

    def exibir_informacoes(self):
        print(f'\nEspécie {self.especie}')
        print(f'Peso {self.peso}')
        print(f'Cor {self.cor}')
        print(f'Idade {self.idade}')



if __name__ == '__main__':
    cavalo_1 = Cavalo(
        especie='Machador',
        idade=10,
        peso=155.50,
        cor='marrom'
    )

    cavalo_2 = Cavalo(
        especie='Machador',
        idade=12,
        peso=160.50,
        cor='preto'
    )

    gato_objeto = Gato(
        especie='Ciemes',
        idade=6,
        peso=2.5,
        cor='laranja'
    )

    cao_obejto = Cachorro(
        especie='Labrador',
        idade=8,
        peso=8.5,
        cor='cinza'
    )

    cavalo_1.exibir_informacoes()
    cavalo_1.emitir_som()
    cavalo_1.mover()
    cavalo_1.comer()

    cavalo_2.exibir_informacoes()
    cavalo_2.emitir_som()
    cavalo_2.mover()
    cavalo_2.comer()

    gato_objeto.exibir_informacoes()
    gato_objeto.emitir_som()
    gato_objeto.mover()
    gato_objeto.comer()

    cao_obejto.exibir_informacoes()
    cao_obejto.emitir_som()
    cao_obejto.mover()
    cao_obejto.comer()



    



