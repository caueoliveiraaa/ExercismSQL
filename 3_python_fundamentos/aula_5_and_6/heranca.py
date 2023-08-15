# classe mãe
class Animal:
    def __init__(self, nome, cor):
        self.nome = nome 
        self.cor = cor

    def correr(self):
        print(f'\U0001F1E6 {self.nome} está correndo...') 

    def comer(self):
        print(f'\U0001F1E6 {self.nome} está se alimentando...') 


# subclasse herdando classe animal
class Cachorro(Animal):
    def latir(self):
        print('\U0001F436 Au au - I am a dog !!')


# subclasse herdando classe animal
class Gato(Animal):
    def destruir_sofa(self):
        print('\U0001F63A Seu sofá foi destruídto pelas patas maliginas !!!')

    def miar(self):
        print('\U0001F63A meau meau')


cao_1 = Cachorro('bryan', 'black')
cao_1.comer()
cao_1.correr()
cao_1.latir()

gato_1 = Gato('vixano', 'white')
gato_1.comer()
gato_1.correr()
gato_1.destruir_sofa()
gato_1.miar()
