#cpf = input ("Insira seu CPF (xxx.xxx.xxx-xx): ")

# def verificadorCPF(cpf):
#     if len(cpf) != 14:
#         return False

#     else:
#         soma1 = 0
#         novo1 = ""

#         for i in cpf:
#             if i!="." and i!="-":
#                 novo1+=i

#     #numeros de 1-9 sendo multiplicados por 10-2

#         novo2 = ""
#         x=2

#         for i in novo1[8::-1]:
#             novo2 = i + novo2
#             soma1+=(int(i)*x)
#             x+=1

#     #cálculo do primeiro digito

#         primerio_digito = 11 - ( soma1%11 )
#         if primerio_digito==10:
#             primerio_digito = 0

#         digitos = novo2 + str(primerio_digito)

#     #segundo digito verificador

#         soma2 = 0
#         novo4 = ""
#         y=2

#         for i in novo1[9::-1]:
#             novo4 = i + novo4
#             soma2+=(int(i)*y)
#             y+=1

#         segundo_digito = 11 - (soma2%11)

#         if segundo_digito==10:
#             segundo_digito=0

#         digitos += str(segundo_digito)

#     #verificador

#         if cpf[12]==str(primerio_digito) and cpf[13]==str(segundo_digito):
#             return True
#         else:
#             return False


#Verficador de CPF by Mayumi

import mysql.connector
from Funcionario import *
from ConnectionFactory import *

def VerificaDigitos(cpf):
    soma1 = 0
    novo1 = ""
    for i in cpf:
        if i!="." and i!="-":
            novo1+=i    
    novo2 = ""
    x=2
    for i in novo1[8::-1]:
        novo2 = i + novo2
        soma1+=(int(i)*x)
        x+=1
    primerio_digito = 11 - ( soma1%11 )
    if primerio_digito>=10:
        primerio_digito = 0

    digitos = novo2 + str(primerio_digito)
    soma2 = 0
    novo4 = ""
    y=2
    for i in novo1[9::-1]:
        novo4 = i + novo4
        soma2+=(int(i)*y)
        y+=1
    segundo_digito = 11 - (soma2%11)
    if segundo_digito>=10:
        segundo_digito=0
    digitos += str(segundo_digito)
    if cpf[12]==str(primerio_digito) and cpf[13] == str(segundo_digito):
        return True
    else: 
        return False
    
def VerificaExistencia(cpf):
    conexao = ConnectionFactory().getConexao()
    cursor = conexao.cursor()
    sql = 'SELECT COUNT(*) FROM FUNCIONARIO WHERE CPF = %s'
    cursor.execute(sql, (cpf,))
    quantidade_registros = cursor.fetchone()[0]
    if quantidade_registros == 0:
        return True
    else: 
        return False

def VerificarCPF(msg):
    while True:
        try:
            cpf = str(input(msg))
            # while len(cpf)!=14: 
            #     print("\033[31mCPF inválido, digite 14 dígitos!\033[m")
            #     cpf = str(input(msg))
            # while cpf[12]!=str(primerio_digito) or cpf[13]!=str(segundo_digito):
            #     print("\033[31mCPF inválido!\033[m")
            #     cpf = str(input(msg))
            
            #Verificar se ja existe

            #print(quantidade_registros)
            while len(cpf) != 14 or VerificaDigitos(cpf)==False or VerificaExistencia(cpf)==False:
                print("\033[31mCPF inválido ou já existe no banco de dados. Tente novamente.\033[m")
                cpf = str(input(msg))
            return cpf
                # if quantidade_registros > 0:
                #     print(f"ERRO! Já existe um(a) funcionário(a) com o CPF {cpf}.")
                #     cpf = str(input(msg))
                # if len(cpf)!=14: 
                #     print("\033[31mCPF inválido, digite 14 dígitos!\033[m")
                #     cpf = str(input(msg))
                # if cpf[12]!=str(primerio_digito) or cpf[13]!=str(segundo_digito):
                #     print("\033[31mCPF inválido!\033[m")
                #     cpf = str(input(msg))

        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido. \033[m")
            continue
        #except Exception as err:
        #   print (f"Erro no CPF: {err}")
        
# cpf1 = "802.022.199-92"
# cpf2 = "483.506.338-40"

# print(VerificaDigitos(cpf1))
# print(VerificaExistencia(cpf1))
# print(VerificaDigitos(cpf2))
# print(VerificaExistencia(cpf2))
# print(len(cpf1))
# print(len(cpf2))
        
