# 3 - Classe Carro:
# Crie uma classe chamada Carro que simule um carro.
#  A classe deve ter os atributos marca, modelo e ano.
# Crie métodos para ligar (ligar()), desligar (desligar()) e exibir as
# informações do carro (exibir_informacoes()).

class Carro:
    marca = 'Nissan'
    modelo = 'Kicks'
    ano = 1990

    def ligar():
        print('O carro ligou!')

    def desligar():
        print('O carro desligou!')

    def exibir_informacoes():
        print(
            f'Este carro é do ano {Carro.ano}, marca {Carro.marca}, modelo {Carro.modelo}.'
        )


while True:
    methodo = input('Informe o nome do método (s = para sair): ')

    if methodo.lower() == 'ligar':
        Carro.ligar()
    elif methodo.lower() == 'desligar':
        Carro.desligar()
    elif methodo.lower() == 'exibir':
        Carro.exibir_informacoes()
    elif methodo.lower() == 's':
        print('programa encerrado.')
        break

