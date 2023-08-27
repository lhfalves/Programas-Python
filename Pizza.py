# Escolha de Pizza
# pequeno sistema de escolha de pizza com Menu
# exibição das escolhas e valores
# melhor visualizado no prompt de comando

from datetime import date, time, datetime
import os
import locale

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8') #formata o número como PT-BR

pizza_escolhida = {}  # definição de dicionário
vl, tot = 0, 0


def trabalhando_com_datetime(argumento):
    data_atual = datetime.now()
    print(argumento, data_atual.strftime('%d/%m/%y %H:%M:%S'))


def formata_tela():
    print(50 * "/", "Pizza do Zé", 50 * "/")
    # print("\n")


#def converte_em_real(vlr):
 #   converte = float(vlr)
  #  valor_em_Real_formatado = locale.currency(converte)
  #  return valor_em_Real_formatado



status = True
while status:

    menu = ['calabreza', 'peperone', 'quatro queijos', 'frango', 'portuguesa', 'escarola', 'napolitana', 'toscana',
            'mussarela', 'marguerita']
    cobertura = ['calabreza fatiada, cebola e azeitona preta',
                 'Pepperoni, mussarela e azeitona preta',
                 'Parmesão, provolone, catupiry, gorgonzola e azeitona preta',
                 'frango desfiado, catupiry e azeitona preta',
                 'presunto, ovos,cebola, azeitona verde e mussarela',
                 'escarola no alho, mussarela e azeitona verde',
                 'mussarela, molho de tomate, parmesão e azeitona preta',
                 'mussarela, calabresa moida e azeitona preta',
                 'mussarela e azeitona preta',
                 'mussarela, rodelas de tomate, manjericão e azeitona preta']

    preco = ['37.00', '40.00', '39.00', '35.00', '42.00', '41.00', '48.00', '50.00', '37.00', '49.00']

    os.system("cls")
    trabalhando_com_datetime('Data de Hoje :')
    formata_tela()
    print("\t\t\t Sabores de Pizzas :", "\n")

    for x in menu:
        print("\t\t\t\t\t\t\t\t", menu.index(x), "  :", x.title(), "\n")

    formata_tela()

    try:
        a = int(input('Entre com o número correspondente a escolha da pizza: '))
    except ValueError:
        a = 100

    if a > len(menu) - 1 or a < 0:
        print( "\n")
        print("Você digitou uma opção que não existe no Menu")
        print("Selecione a opção numerica para escolher sua pizza")
        print( "\n")
        os.system("pause")  # força uma pausa no programa

    else:

        vl = vl + 1  # quantidade de pizzas compradas
        print("Pedido:", vl)
        print("Você escolheu a Pizza :           ", "\t", menu[a].title())
        print("Esse sabor possui a cobertura de :", "\t", cobertura[a].title())
        converte = float(preco[a])
        valor_em_Real_formatado = locale.currency(converte, grouping=True, symbol=None )
        print("O preço desta Pizza é de : R$", "\t\t", valor_em_Real_formatado )
        print(30 * '*', "Bom apetite !")
        tot = tot + float(preco[a]) # total gasto

        pizza_escolhida[menu[a].title()] = preco[a]  # armazena em dicionário o nome da pizza e o valor

        print(" Deseja pedir uma nova pizza ?")
        escolha = input('( s ou n ? )')
        if escolha == "n":

            os.system("cls")
            formata_tela()
            trabalhando_com_datetime('Data da Compra: ')
            valor_em_Real_formatado = locale.currency(tot,  grouping=True, symbol=None )
            print('Você comprou {}'.format(vl), ' pizza(s) e gastou o total de R$: ', valor_em_Real_formatado)
            print("Descrição da(s) compra(s) : ")

            # nesse for se percorre o dicionário e lista o nome e o valor
            for sabor, preco in pizza_escolhida.items():
                converte = float(preco)
                valor_em_Real_formatado = locale.currency(converte,  grouping=True, symbol=None )
                print("Sabor da pizza: ", sabor, '- Preço da pizza : R$ ', valor_em_Real_formatado)

            formata_tela()
            print("\n")
            os.system("pause")

            os.system("cls")
            formata_tela()

            print("Voltar ao menu de pizzas (s) ou encerrar o programa (n) ? ")
            escolha = input('( s ou n ? )')
            if escolha == "n":
                print(' Fim do programa \n')
                status = False
            else:
                pizza_escolhida = {}  # definição de dicionário
                vl, tot = 0, 0
