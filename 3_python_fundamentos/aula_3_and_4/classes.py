class ClasseCachorro:
    # atributos = variaveis
    raca = 'Pastor Alemão'
    idade = 5

    # métodos - funções
    def latir(latidas):
        for latida in range(latidas):
            print('au au')

    def comer(comida, horario):
        print(f'au au, comi {comida}, au au em horario {horario}')
        
    def mostrar_info_dog():
        print(f'O cachorro é da raça {ClasseCachorro.raca} e tem {ClasseCachorro.idade} anos')

class ClassePessoa:
    # atributos = variaveis
    nome = 'Caue'
    idade = 26
    altura = 1.80
    peso = 105
    pais_origem = 'Brasil'
    genero = 'Alien'

    # métodos - funções
    def dizer_ola():
        print(f'Olá, eu sou {ClassePessoa.nome}')

    def mostrar_dados():
        print(
            f'Eu tenho {ClassePessoa.idade} anos, {ClassePessoa.altura} altura,' +
            f'{ClassePessoa.peso}, peso e meu genero é {ClassePessoa.genero}'
        )

    def mostrar_origem():
        print(f'Eu venho de/do/da {ClassePessoa.pais_origem}')

ClasseCachorro.latir(10)
ClasseCachorro.comer('ração', '10:00 am')
ClasseCachorro.mostrar_info_dog()
# ClassePessoa.dizer_ola()
# ClassePessoa.mostrar_dados()
# ClassePessoa.mostrar_origem()
    