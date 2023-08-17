# 2 - Crie uma classe Banco com métodos abstratos depositar(), ver_saldo() e sacar() e 
# implemente a lógica de cada método. Crie subclasses ContaCorrente e ContaPoupanca
# que herdam da classe Banco e implementam os métodos de acordo com suas regras específicas.
# Por exemplo, a subclasse ContaPoupanca pode nao deter o método sacar().
# Crie atributos privados e publicos nas subclasses ContaCorrente e ContaPoupanca
# como self.nome, self.saldo, e self.numero_conta por exemplo. Crie objetos dessas
# classes com informações distintas, invoque os métodos e printe o resultado das
# operações. 

from abc import ABC, abstractmethod


class Banco(ABC):
    def __init__(self, nome, saldo, numero_conta):
        self.nome = nome
        self.__saldo = saldo
        self._numero_conta = numero_conta

    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def ver_saldo(self):
        pass
    
    @abstractmethod
    def sacar(self):
        pass


class ContaCorrente(Banco):
    def depositar(self, deposito):
        if deposito > 0:
            self._Banco__saldo += deposito
            print('Depósito realizado com sucesso.')
        else:
            print('Informe um depósito acima de zero!')

    def ver_saldo(self):
        return self._Banco__saldo

    def sacar(self, valor_a_sacar):
        self._Banco__saldo -= valor_a_sacar
        print(f'Saque de R$ {valor_a_sacar} realizado com sucesso.')


class ContaPoupanca(Banco):
    def depositar(self, deposito):
        if deposito > 0:
            self._Banco__saldo += deposito
            print('Depósito realizado com sucesso.')
        else:
            print('Informe um depósito acima de zero!')
    
    def ver_saldo(self):
        return self._Banco__saldo

    def sacar(self):
        print('Não são permitidos saques em conta poupança!')


conta_1 = ContaPoupanca('rodrigo', 500, 11651)
conta_1.sacar()
print(conta_1.ver_saldo())
conta_1.depositar(100)
print(conta_1.ver_saldo())

print('\n')

conta_2 = ContaCorrente('adrian', 6000, 25151)
print(conta_2.ver_saldo())
conta_2.sacar(2000)
print(conta_2.ver_saldo())
conta_2.depositar(10000)
print(conta_2.ver_saldo())
