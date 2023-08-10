
class Animal:
    # PRIVATE -> __nome
    # PROTECTED -> _nome
    # PUBLIC = nome

    # CONSTRUTOR
    def __init__(self, raca, cor, idade, nome):
        self._raca = raca # protected
        self._cor = cor # protected
        self._idade = idade # protected
        self.__nome = nome # private
        print('Objeto instanciado com sucesso.')

    # GETTERS COM @property

    @property
    def raca(self):
        return self._raca


    @property
    def cor(self):
        return self._cor


    @property
    def idade(self):
        return self._idade
    

    @property
    def nome(self):
        return self.__nome


    # SETTERS COM variavel.setter

    @raca.setter
    def raca(self, raca_nova):
        print(f'Setou raça {self._raca} para {raca_nova}')
        self._raca = raca_nova


    @cor.setter
    def cor(self, cor_nova):
        print(f'Setou cor {self._cor} para {cor_nova}')
        self._cor = cor_nova


    @idade.setter
    def idade(self, idade_nova):
        print(f'Setou idade {self._idade} para {idade_nova}')
        self._idade = idade_nova


    @nome.setter
    def nome(self, nome_novo):
        print(f'Setou nome {self.__nome} para {nome_novo}')
        self.__nome = nome_novo


if __name__ == '__main__':
    # INSTANCIAS (CRIAÇÕES) DOS OBJETOS DA CLASSE ANIMAL
    leao = Animal('leao da montanha', 'bege', 15, 'simba')
    gato = Animal('ciemes', 'preto', 11, 'vixano')
    pantera = Animal('pantera cor de rosa', 'rosa', 19, 'king')
    # UTILIZAR GETTERS PARA CADA OBJETO
    print(leao.raca)
    print(leao.cor)
    print(leao.idade)
    print(gato.raca)
    print(gato.cor)
    print(gato.idade)
    print(pantera.raca)
    print(pantera.cor)
    print(pantera.idade)
    # UTILIZAR SETTERS
    pantera.idade = 56
    print(pantera.idade)
    pantera.cor = 'verde'
    gato.raca = 'Persa'
    print(pantera.nome)