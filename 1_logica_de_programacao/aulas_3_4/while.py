

# indice = 1
# while indice <= 10:
#     print(f'Infice {indice}')
#     indice += 1
    
# indice_2 = 10
# while indice_2 >= 0:
#     print(f'Infice {indice_2}')
#     indice_2 -= 1


numero = int(input('Informe um numero: '))



# Parando loop manualmente
comando = ''
rodar_loop = True
while rodar_loop == True:
    comando = input(
        'Informe 1 para continuar e 0 para parar: '
    )
    
    if comando != '1':
        print('Parou loop!')
        rodar_loop = False

i = 0
while i < 5:
    try:
        print(i)
    except Exception as e:
        print(e) 

    i += 1
