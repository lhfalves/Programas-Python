from datetime import date, time, datetime

# -----------Menu de atualização -------------------------------
def menu():
    print("\n")
    print( 20 * "/", " Menu ", 20 * "/")
    print("[d] Depositar ")
    print("[s] Sacar")
    print("[e] Extrato")
    print("[q] Sair")

    return


saldo = 0
limite = 500
extrato, sld = "", ""
numero_saques = 0
LIMITE_SAQUES = 3


# -----------Atualização de datas do sistema -------------------------------
def atualiza_data():
    data_atual = datetime.now()
    #print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    dt = str(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    return dt

# -----------Testa inconsistências do valor digitado pelo usuário -------------------------------
def teste_erro():
    try:
        valor = float(input('Digite o valor: '))
    except ValueError:
        print("Valor informado inválido ")
        valor = 0
    else:
        if valor < 0:
            print("Informar um valor positivo")
            valor = 0
    finally:
        return valor


# -----------Verifica se a data atual é a mesma do extrato. -------------------------------
def testa_limite_saque():
    # Verifica se a data atual (dt) é a mesma do extrato.
    # Caso negativo permite retorno do limite de saque para 3

    data_sist = atualiza_data()
    data_sist = data_sist[0:8]
    # localiza a última ocorrência da barra da data
    localizastring = extrato.rfind('/')
    # manipula a string e fatia a parte da data
    fatia = extrato[localizastring - 5: localizastring + 3]
    # Caso a a data atual seja diferente da última data do extrato volta o LIMITE de Saque para 3

    if data_sist != fatia:
        return True
    else:
        return False

# ---------Recebe os argumentos saldo, extrato por nome (positional Only Arguments). -----
def depositar(saldo, extrato, /):
    # função de deposito
    print(" Opção Depósito ", 20 * "/")
    print("Qual valor deseja depositar ? ")

    valor_depositado = teste_erro()

    if valor_depositado > 0:

        saldo = saldo + valor_depositado
        # atualiza a data do depósito
        dt = atualiza_data()
        extrato = extrato + str(dt) + f" R${valor_depositado:,.2f}" + " Depósito" + "\n"

    return saldo, extrato


# ---------Recebe os argumentos saldo, extrato e LIMITE_SAQUES por nome (Keyword-Only Arguments). -----
def sacar(*, saldo, extrato, LIMITE_SAQUES ):

    if testa_limite_saque(): LIMITE_SAQUES = 3

    # testa o limite de saques
    if LIMITE_SAQUES > 0:
        print("Opção Saque ", 20 * "/")
        print("Saldo atual :", saldo)
        print(" Qual valor deseja sacar ? ")
        valor_saque = teste_erro()

        if valor_saque > 0 and valor_saque < 501:
            # teste_saldo verifica se o saldo ficara menor do que zero
            teste_saldo = saldo - valor_saque

            if teste_saldo >= 0:
                    LIMITE_SAQUES = LIMITE_SAQUES - 1
                    saldo = saldo - valor_saque

                    # atualiza data do saque
                    dt = atualiza_data()
                    extrato = extrato + str(dt) + f" R${valor_saque:,.2f}" + " Saque" + "\n"
            else:
                    print(" Saldo insuficiente para realizar este saque! Operação não realizada")

        else:
            print(" Escolha um valor positivo e menor do que R$ 500,00")
    else:
        print("Você excedeu o limite de saques nesta data. Operação não realizada ")

    return saldo, extrato, LIMITE_SAQUES


# ---------Recebe os argumentos saldo; e extrato por nome (Keyword-Only Arguments). -----
def exibir_extrato(saldo,  *,extrato):

    print(" Opção Extrato ", 20 * "/")
    # evita erro caso o usuáro escolha extrato sem saldo
    if len(extrato) > 0:
        print(extrato)

    print(f"Saldo em conta: R${saldo:,.2f}")
    print(20 * "/")


while True:

    menu()
    opcao = input("Selecione uma opção: ")

    # opção de depósito =================================================
    if opcao == "d":

        saldo, extrato = depositar(saldo, extrato)

    # opção de saque =====================================================
    elif opcao == "s":

        if saldo > 0 :
            saldo, extrato, LIMITE_SAQUES = sacar(
                saldo=saldo,
                extrato=extrato,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )
        else:
            print(" Sua conta não possui saldo. Deposite algum valor na conta!")

    # opção de extrato =====================================================
    elif opcao == "e":

        exibir_extrato(saldo, extrato=extrato)


    # opção de sair do programa =============================================
    elif opcao == "q":
        print(" Sair ")
        break

    else:
        print(" Opção inválida! Por favor, selecione a opção do Menu.")



