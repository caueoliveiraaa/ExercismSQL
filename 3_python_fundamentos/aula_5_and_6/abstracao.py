from abc import ABC, abstractmethod


class PessoaAbstrata(ABC):
    @abstractmethod
    def gastar_dinheiro():
        pass

    @abstractmethod
    def respirar():
        pass

    @abstractmethod
    def falar():
        pass


class Atleta(PessoaAbstrata):
    def gastar_dinheiro():
        print('Eu gasto pouco dinehrio!')

    def falar():
        print('Queremos um aumento!')

    def respirar():
        print('Estou respirando profundamente!')


class Artista(PessoaAbstrata):
    def gastar_dinheiro():
        print('Eu gasto muito dinehrio porque eu posso!')

    def falar():
        print('Eu sou rico e falo 5 idiomas!! How are you baby?')

    def respirar():
        print('Eu sou pago até para respirar!')


if __name__ == '__main__':
    Artista.gastar_dinheiro()
    Atleta.gastar_dinheiro()
    Artista.falar()
    Atleta.falar()
    Artista.respirar()
    Atleta.respirar()
