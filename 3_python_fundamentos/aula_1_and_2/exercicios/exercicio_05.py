# Exercício 5:
# Crie uma função que exiba uma mensagem perguntando a idade do usuário e,
# com base na idade fornecida, exiba diferentes mensagens de acordo com as
# seguintes faixas etárias: 0-12 anos, 13-17 anos, 18 ou mais anos.
# (mais faixas etárias podem ser incluídas)

def busque_idade_valida():
    idade = 0
    while True:
        try:
            idade = int(input('Informe a idade: ')) 
            break
        except:
            print('Informe uma idade válido!')
    
    return idade


def valida_faixa_etaria(idade):
    if idade > 0 and idade < 150:
        if idade <= 12:
            print('Criança')
        elif idade < 18:
            print('Teen')
        else:
            print('Adulto!')
    else:
        print(f'Você informou uma idade inválida -> {idade}')


if __name__ == '__main__':
    idade = busque_idade_valida()
    valida_faixa_etaria(idade)





