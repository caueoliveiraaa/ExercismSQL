# Crie uma classe chamada Triangulo que represente um triângulo.
#  A classe deve ter os atributos lado1, lado2 e lado3.
# Crie métodos para verificar se os lados formam um triângulo válido (eh_valido()), 
# calcular o perímetro (calcular_perimetro())
# e exibir o tipo do triângulo com base nos lados (tipo_triangulo()).

class Triangulo:
    def __init__(self, lado_1, lado_2, lado_3):
        self._lado_1 = lado_1
        self._lado_2 = lado_2
        self._lado_3 = lado_3
        print('Objeto instanciado com sucesso.')


    def eh_valido(self):
        lado_1_valido = (self._lado_3 + self._lado_2) > self._lado_1
        lado_2_valido = (self._lado_1 + self._lado_3) > self._lado_2
        lado_3_valido = (self._lado_1 + self._lado_2) > self._lado_3

        return lado_1_valido is True and lado_2_valido is True and lado_3_valido is True
     

    def calcula_perimetro(self):
        return (self._lado_1 + self._lado_2 + self._lado_3)
        

    def tipo_triangulo(self):
        if (self._lado_1 == self._lado_2) and (self._lado_1 == self._lado_3): 
            print('Este triângulo é equilátero!')
        elif (self._lado_1 != self._lado_2) and (self._lado_1 != self._lado_3) and (self._lado_2 != self._lado_3): 
            print('Este triângulo é escaleno!')
        else:
            print('Este triângulo é isóceles!')



if __name__ == '__main__':
    triangulo_1 = Triangulo(lado_1=4.6, lado_2=6.8, lado_3=7.1)
    triangulo_2 = Triangulo(lado_1=3.1, lado_2=3.7, lado_3=5.2)
    triangulo_3 = Triangulo(lado_1=3, lado_2=3, lado_3=3)
    triangulo_4 = Triangulo(lado_1=3, lado_2=3, lado_3=2)

    print(f'Triânguo 1 é válido: {triangulo_1.eh_valido()}')
    print(f'Triânguo 2 é válido: {triangulo_2.eh_valido()}')
    print(f'Triânguo 3 é válido: {triangulo_3.eh_valido()}')
    print(f'Triânguo 4 é válido: {triangulo_4.eh_valido()}')

    print(f'Triânguo 1 - perímetro: {triangulo_1.calcula_perimetro()}')
    print(f'Triânguo 2 - perímetro: {triangulo_2.calcula_perimetro()}')
    print(f'Triânguo 3 - perímetro: {triangulo_3.calcula_perimetro()}')
    print(f'Triânguo 4 - perímetro: {triangulo_4.calcula_perimetro()}')

    triangulo_1.tipo_triangulo()
    triangulo_2.tipo_triangulo()
    triangulo_3.tipo_triangulo()
    triangulo_4.tipo_triangulo()