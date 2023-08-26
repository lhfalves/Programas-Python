# Curso Fundamentos de Linguagem Python Para Análise de Dados e Data Science
# Exercício - minha solução do Lab2 - Calculadora em Linguagem Python 26/08/2023
# Pycharm 2023.2.1 - Python 3.8

from datetime import date, time, datetime
import os

status = True

# - Menu do sistema ===============================
def menu() :

    data_atual = datetime.now().strftime('%d/%m/%y %H:%M:%S')

    print('Data e hora atualizada', data_atual)
    print('\n')
    print(50 * "/", " Calculadora em Python ", 50 * "/", '\n \n')
    print(' Selecione abaixo uma opção de calculo :\n')
    print("  < 1 > - Soma :  \n " +
          " < 2 > - Subtração : \n " +
          " < 3 > - Multiplicação :  \n " +
          " < 4 > - Divisão : \n " +
          " < 5 > - Sair \n")


# modulo de escolha da operação Matemática ===============================
def perguntar():

    opcao = input ("Digite sua opção 1/2/3/4 ou 5 ?")

    return {
    '1':"Escolhida a opção 1 - Soma! ",
    '2':"Escolhida a opção 2 - Subtração! ",
    '3':"Escolhida a opção 3 - Multiplicação! ",
    '4':"Escolhida a opção 4 - Divisão! ",
    '5':"Sair do sistema, opção 5",   }.get(opcao,"Número inválido!")


# Faz o tratamento da operação Matemática ===============================
def operacaoMat( resp ):

   try:
        n1 = float(input ('Digite o primeiro número da '+ resp[22:35] + ' : '))
        n2 = float(input('Digite o segundo número da '+ resp[22:35] + ' : '))
        print('\n')
   except ValueError:
        print('Não foi possível realizar a operação. Valores inválidos! \n')
        os.system("pause")  # força uma pausa no programa

   else :

        if  resp[18] =="1":
            soma = n1 + n2
            print("Resultado: ",n1, "+", n2, "=" , soma)

        elif resp[18]=="2":
             subtracao = n1 - n2
             print("Resultado: ",n1, "-", n2, "=" , subtracao)

        elif resp[18]=="3":
             mult = n1 * n2
             print("Resultado: ",n1, "*", n2, "=" , mult)

        elif resp[18]=="4":
             if n2==0 :
                 print("Divisão Impossível. Escolha um número maior que zero!")
             else:
                 div = n1 / n2
                 print("Resultado: ",n1, "/", n2, "=" , div)


        os.system("pause")  # força uma pausa no programa

###   ===============================


while status:

    menu()   # chama o Meu de opções
    resposta = perguntar() #chama a função de perguntar a opção escolhida
    print(resposta, '\n')

    if resposta == "Número inválido!" :    # Faz o tratamento prévio se o Número for Inválido
         os.system("pause")  # força uma pausa no programa

    elif resposta[23] =="5" :   # Faz o tratamento prévio se a opção for de sair do sistema
         status = False

    else:
        operacaoMat(resposta)  # Chama a funcão de escolha da operação Matemática com o argumento (opcão escolhida)


