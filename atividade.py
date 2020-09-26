import os

os.system('cls') or None

lista = []

print('------------------------------------------------------------------------------------------------------------------------')
print('--------------------------------------------------REGISTRO DE COMPRAS---------------------------------------------------')
print('\nOlá, bem vindo ao programa de lista de compras\n')
print('Para o melhor usufruto do programa, digite o número da lista que deseja\n')
print('Para criar a lista, insira 1\n')
print('Para deletar algum item da lista, insira 2\n')
print('Para ver a lista, insira 3\n')
print('Encerrar o aplicativo, insira 0\n')
print('------------------------------------------------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------------------------------------------------')
print('--------------------------------------------------REGISTRO DE COMPRAS---------------------------------------------------')
opcaoMenu = int(input('O que quer fazer hoje? '))
print('------------------------------------------------------------------------------------------------------------------------')

def segundoMenu(opcaoMenu): #Recupera o menu e recria o laço de repetição
    print('Para criar a lista, insira 1\n')
    print('Para deletar algum item da lista, insira 2\n')
    print('Para ver a lista, insira 3\n')
    print('Encerrar o aplicativo, insira 0\n')
    opcaoMenu = int(input('O que quer fazer hoje? '))
    menu(opcaoMenu)


def inserirProduto(): #Insere novos produtos na lista
    os.system('cls') or None
    print('------------------------------------------------------------------------------------------------------------------------')
    quantidadeProduto = int(input('Quantos produtos irá colocar na lista? '))
    i = 0
    while i < quantidadeProduto:
        inputUsuario = input('Insira o produto: ')
        lista.append(inputUsuario)
        i += 1
    print('------------------------------------------------------------------------------------------------------------------------')
    opcaoMenu = 0
    segundoMenu(opcaoMenu)

def removeLista(): #Retira produtos da lista
    os.system('cls') or None
    print('------------------------------------------------------------------------------------------------------------------------')
    for n in lista:
        print(n,'\n')
    inputUsuario = input('Qual produto deseja retirar?\n')
    lista.remove(inputUsuario)
    print('------------------------------------------------------------------------------------------------------------------------')
    segundoMenu(opcaoMenu)
    print('------------------------------------------------------------------------------------------------------------------------')


def verLista(): #Imprime a Lista
    os.system('cls') or None
    print('------------------------------------------------------------------------------------------------------------------------')
    for n in lista:
        print(n,'\n')
    print('------------------------------------------------------------------------------------------------------------------------')
    segundoMenu(opcaoMenu)
    print('------------------------------------------------------------------------------------------------------------------------')


def fimMenu():
    print('------------------------------------------------------------------------------------------------------------------------')
    print('Muito obrigado por usar este programa. Até a próxima!')
    print('------------------------------------------------------------------------------------------------------------------------')

def menu(opcaoMenu):
    if opcaoMenu == 1:
        inserirProduto()
    elif opcaoMenu == 2:
        removeLista()
    elif opcaoMenu == 3:
        verLista()
    else:
        fimMenu()

menu(opcaoMenu)