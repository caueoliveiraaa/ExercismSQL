# Crie uma classe chamada Agenda que represente uma agenda de contatos.
#  A classe deve ter um atributo para armazenar uma lista de contatos.
# Crie métodos para adicionar (adicionar_contato(nome, telefone)), remover (remover_contato(nome)),
#  e exibir todos os contatos (exibir_contatos()).
import os

class Agenda:
    lista_contatos = []

    def adicionar(item_lista):
        Agenda.lista_contatos.append(item_lista)
        print(f'Nome {item_lista[0]} e telefône {item_lista[1]} adicionado com sucesso!')


    def remover(posicao):
        Agenda.lista_contatos.pop(posicao)
        print(f'Item na posição {posicao} removido com sucesso!')


    def exibir_info():
        if len(Agenda.lista_contatos) > 0:
            for i in range(len(Agenda.lista_contatos)):
                print(f'\33[032mPosição -> {i} nome -> {Agenda.lista_contatos[i][0]} telefone -> {Agenda.lista_contatos[i][1]}\33[0m')
        else:
            print('A lista está vazia!')


    def rodar_script():
        while True:
            try:
                methodo = input('Informe o método (s para sair): ')

                if methodo.lower() == 'adicionar':
                    novo_nome = input('Informe o novo nome: ')
                    novo_telefone = input('Informe o novo telefône: ')
                    Agenda.adicionar([novo_nome, novo_telefone])
                elif methodo.lower() == 'remover':
                    posicao = int(input('Informe a posição: '))
                    Agenda.remover(posicao)
                elif methodo.lower() == 'exibir':
                    Agenda.exibir_info()
                elif methodo.lower() == 's':
                    print('Programa encerrado.')
                    break
            except Exception as erro:
                print(f'Ocorreu um erro: {erro}')


if __name__ == '__main__':
    os.system('cls')
    Agenda.rodar_script()