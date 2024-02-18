
from Restaurante import *
def verificarArquivo(arquivo): # verifica se o arquivo existe
    try:
        a = open(arquivo, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(arquivo):
    try:
        a = open(arquivo, "wt+")
    except:
        print("\033[31mOcorreu algum erro na criação do arquivo!\033[m")
    else:
        print(f"Arquivo {a} criado com sucesso!")


def cadastrar(arquivo, lista):
    try:
        a = open (arquivo, "wt+")
    except:
        print("\033[31mHouve um Erro na abertura do arquivo!\033[m")
    else:
        try:
            for restaurante in lista:
                a.write(f"{restaurante.nome};{restaurante.endereco};{restaurante.telefone};{restaurante.cep};{restaurante.nota}\n")
        except:
            print("\033[31mHouve um Erro na hora de escrever os dados!\033[m")
        else:
            print(f"\033[35m\033[1mNovo registro de {restaurante.nome} adicionado!\033[m")
            a.close()

def alterar(arquivo, lista, res):
    try:
        a = open (arquivo, "wt+")
    except:
        print("\033[31mHouve um Erro na abertura do arquivo!\033[m")
    else:
        try:
            for restaurante in lista:
                a.write(f"{restaurante.nome};{restaurante.endereco};{restaurante.telefone};{restaurante.cep};{restaurante.nota}\n")
        except:
            print("\033[31mHouve um Erro na hora de escrever os dados!\033[m")
        else:
            print(f"\033[32m\033[1mRegistro de {res.nome} alterado com sucesso!\033[m")
            a.close()

def lerArquivo(arquivo):
    try:
        a = open(arquivo,"rt")
    except:
        print("Erro ao ler o arquivo!")
    else:
        lista = []
        for linha in a:
            dado = linha.split(";")
            dado[len(dado)-1] = dado[len(dado)-1].replace("\n","") #tirar quebra do fim
            lista.append(Restaurante(dado[0], dado[1], dado[2], dado[3], dado[4]))
        return lista
            # print(f"{dado[0]:<30}{dado[1]:>3}")
    finally:
        a.close()