
dia_nome = ''
dia_numero = int(input('Infomre o dia: '))

match dia_numero:
    case 0:
        dia_nome = 'Domingo'
    case 1:
        dia_nome = 'Segunda-feira'
    case 2:
        dia_nome = 'Terça-feira'
    case 3:
        dia_nome = 'Quarta-feira'
    case 4:
        dia_nome = 'Quinta-feira'
    case 5:
        dia_nome = 'Sexta-feira'
    case 6:
        dia_nome = 'Sábado'
    case _:
        dia_nome = 'Input inválido'

if dia_numero >= 0 and dia_numero <= 6:
    print(dia_nome)
else:
    print('Numero invalido para dia da semana')