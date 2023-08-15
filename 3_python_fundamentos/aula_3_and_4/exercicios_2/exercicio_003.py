# 3- - Classe Conta Bancária:
# Crie uma classe chamada ContaBancaria, com os atributos saldo (private),
# titular (public), numero_conta (private). Crie métodos get_saldo() e
# set_saldo(novo_saldo) para acessar e modificar o saldo.

class ContaBancaria:
    def __init__(self, saldo, numero_conta, titular):
        self.__saldo = saldo
        self.__numero_conta = numero_conta
        self.titular = titular

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, saldo_novo):
        self.__saldo = saldo_novo 
    

if __name__ == '__main__':
    conta_1 = ContaBancaria(saldo=100, numero_conta=15, titular='bruno')
    conta_2 = ContaBancaria(saldo=200, numero_conta=16, titular='bruna')

    print(conta_1.titular)
    print(f'Saldo: {conta_1.saldo}')
    print(conta_2.titular)
    print(f'Saldo: {conta_2.saldo}')

    print('\n')

    conta_1.saldo = 500
    conta_2.saldo = 600

    print(conta_1.titular)
    print(f'Saldo: {conta_1.saldo}')
    print(conta_2.titular)
    print(f'Saldo: {conta_2.saldo}')

        

