# Programas-Python
# Fazendo conversao de grandeza
# faz a conversão de temperaturas e medidas
# programa manipulando listas
# também pode ser executado pelo prompt de comando

import os

def Fahrenheit (vlr): # Fahrenheit em Celsius
    formula = float ( vlr - 32) / 1.8
    return formula

def Celsius (vlr):  # Celsius para Fahrenheit
    formula = (vlr * 1.8) + 32
    return formula

def Polegadas (vlr):  # polegada para centimetros
    formula = (vlr * 2.54)
    return formula

def Centimetros (vlr):  # cm para polegadas
    formula = (vlr /2.54)
    return formula

def Kilometro (vlr):  # milha para kilometro
    formula = (vlr * 1.6)
    return formula

def Milha (vlr):  # kilometro para milha
    formula = (vlr / 1.6)
    return formula

def Libra (vlr):  # libra para Kg
    formula = (vlr * 0.453592)
    return formula

def Kilo (vlr):  # kg para libra
    formula = (vlr * 2.205)
    return formula

def formata_tela():
    os.system("cls")
    print(50 * "/", "Conversor ", 50 * "/")
    print("\n")

def mensagem (arg):
    print(arg)
    print("\n")
    os.system("pause")  # força uma pausa no programa


Tipo = ['Fahrenheit para Celsius - opção 0', 'Celsius para Fahrenheit - opção 1',
        'Polegadas para Centímetros - opção 2', 'Centímetros para Polegadas - opção 3',
        'Quilômetros para Milhas - opção 4', 'Milhas para Quilômetros - opção 5',
        'Libras para Kilos - opção 6', 'Kilos para Libras - opção 7',
        'Fahrenheit', 'Celsius',
        'Polegadas','Centímetros',
        'Quilômetros', 'Milhas',
        'Libras', 'Kilos']



testador = True
while testador:

    try :
        formata_tela()
        for c in range(8):
            print('Converter de ', Tipo[c])

        print("\n")
        a = int( input('digite a opção 0 ou 7 ? '))
        print("\n")

        if a > 0 and a < 8 :
            testador = False
        else:
            mensagem("Você escolheu uma opção fora do intervalo do Menu")


    except ValueError:
        a=10
        mensagem("Favor digitar uma opção númerica 0 a 7")


# testagem de valores de entrada
testador = True
while testador:
    try:
        if a==0 or a==1:
            msg = 'a temperatura'
        elif a == 4 or a == 5:
            msg = 'a distância'
        elif a==6 or a ==7:
            msg = 'o peso'
        else:
            msg = 'a medida'

        print("Escolha ", msg , " em", Tipo[a + 8], ": ?")
        vlr = float(input("Digite o valor: ?"))

        if (a==0 or a==1) and (vlr>500 or vlr<-500):
            mensagem("Opção inválida!")

        else:
            testador = False

    except ValueError:
        mensagem("Você digitou uma valor inválido! ")


if a == 0 :
    result = Fahrenheit(vlr)
    texto = Tipo[8] + ' para '+Tipo[9]

elif a == 1 :
    result = Celsius(vlr)
    texto = Tipo[9] + ' para '+Tipo[8]

elif a == 2:
    result = Polegadas(vlr)
    texto = Tipo[10] + ' para ' + Tipo[11]

elif a == 3:
    result = Centimetros(vlr)
    texto = Tipo[11] + ' para ' + Tipo[10]

elif a == 4:
    result = Kilometro(vlr)
    texto = Tipo[12] + ' para ' + Tipo[13]

elif a == 5:
    result = Milha(vlr)
    texto = Tipo[13] + ' para ' + Tipo[12]

elif a == 6:
    result = Libra(vlr)
    texto = Tipo[14] + ' para ' + Tipo[15]

elif a == 7:
    result = Kilo(vlr)
    texto = Tipo[15] + ' para ' + Tipo[14]

print (' Valor convertido de ', vlr , texto , ': ', result)
