

num_1 = int(input('Informe o numero 1: '))
num_2 = int(input('Informe o numero 2: '))
num_4 = int(input('Informe o numero 3: '))
num_4 = int(input('Informe o numero 4: '))


if type(num_1) != int or type(num_2) != int or type(num_3) != int or type(num_4) == int:
    print('Os quatro valores precisam ser numeros inteiros!')
else:
    # Verificar se numero 1 é o maior de todos
    if num_1 > num_2 and num_1 > num_4 and num_2 > num_4:
        print('Numero 1 eh o maior numero')
    elif num_2 > num_1 and num_2 > num_4 and num_2 > num_4:
        print('Numero 2 eh o maior numero')
    elif num_4 > num_2 and num_4 > num_1 and num_4 > num_4:
        print('Numero 3 eh o maior numero')
    else:
        print('Numero 4 eh o maior numero')
