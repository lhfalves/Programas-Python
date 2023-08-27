# Modelo de Programa em Python usando manipulação de arquivo JSON

from datetime import date, time, datetime
import json

usuarios={}

def perguntar():
    data_atual = datetime .now().strftime('%d/%m/%y %H:%M:%S')
    print('Data e hora atualizada', data_atual)
    print(50 * "/", "Menu", 50 * "/")
    print(" <I> - Para Inserir um usuário \n " +
          " <P> - Para Pesquisar um usuário \n " +
          " <E> - Para Excluir um usuário \n " +
          " <L> - Para Listar todos os usuário \n " +
          " <S> - Sair \n" )
    opcao = input ("Digite a sua opção ?").upper()

    return opcao



def registro():
    print('Registro não localizado \n')


def inserir(dicionario):

     #dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
     #                                                    input("Digite a última data de acesso: "),
     #                                                    input("Qual a última estação acessada: ").upper()]
    teste = True
    while teste:
        login = input("Digite o login: ").upper()
        nome = input("Digite o nome: ").upper()
        data_acesso = input("Digite a última data de acesso: ")
        estacao = input("Qual a última estação acessada: ").upper()

        if login =='' or nome=='' or data_acesso=='' or estacao=='':
                print('Não é permitido deixar registros vazios. Digite novamente! \n')
        else:
                teste = False
                dicionario[login] = [nome,data_acesso,estacao]


def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])
        print('\n')
    else:
        registro()

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
        print("Objeto Eliminado \n")
    else:
        registro()

def listar(dicionario):
    if bool(dicionario) :    #verifica se há dados no arquivo
        for chave, valor in dicionario.items():
            print("Objeto......" )
            print("Login: ", chave)
            print("Dados: ", valor)
            print('\n')
    else:
        print("Não há dados no arquivo \n")

def sair(dicionario):

    if bool(dicionario) :
        arquivo = open("base_dados.json", 'w') # método para gravar um dicionário em um arquivo em Python é usar a função dump() do módulo json
        json.dump(dicionario, arquivo)
        arquivo.close()
        print('Base de dados gravados com sucesso \n')
    else:
        print( "Não há dados para gravar")


# ao inicar o programa abre o arquivo e verifica se há dados
arquivo = open("base_dados.json", 'r') # método para ler um dicionário em um arquivo em Python é usar a função dump() do módulo json
if bool(arquivo) :    #arquivo != None :
    usuarios = json.load(arquivo)

arquivo.close()


status = True
while status:
    opcao = perguntar()

    if opcao=="I":
        inserir(usuarios)

    elif opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))

    elif opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))

    elif opcao == "L":
        listar(usuarios)

    elif opcao == "S":
        sair(usuarios)
        print('Fim do programa \n')
        status = False

    else :
        print('Opção não localizada \n')

