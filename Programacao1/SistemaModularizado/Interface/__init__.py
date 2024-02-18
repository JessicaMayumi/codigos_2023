def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido. \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número. \033[m")
            return 0
        else:
            return n

def leiaIntNota(msg):
    while True:
        try:
            n = int(input(msg))
            if(n>5 or n<0):
                print("\033[31mNota inválida, digite uma nota entre 0 e 5!\033[m")
                n = int(input(msg))

        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido. \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número. \033[m")
            return 0
        else:
            return n
        
def VerificarTelefone(telefone):
    while True:
        try:
            t = input(telefone)
            strTelefone = ""
            count = 0
            while len(t)!=11:
                print("\033[31mNúmero de Telefone inválido, digite apenas 11 número!\033[m")
                t = input(telefone)

            for i in t:
                count += 1
                if count == 1:
                    strTelefone += "(" + i
                elif count == 3:
                    strTelefone += ")" + i
                elif count == 9:
                    strTelefone += "-" + i
                else:
                    strTelefone += i
                    
                    
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido. \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número. \033[m")
            return 0
        finally:
            return strTelefone
            
def VerificarCEP(cep):
    while True:
        try:
            c = str(input(cep))
            strCEP = ""
            count = 0
            while len(c)!=8: 
                print("\033[31mCEP inválido, digite 8 dígitos!\033[m")
                c = str(input(cep))
                
            for i in c:
                count += 1
                if count == 6:
                    strCEP += "-" + i
                else:
                    strCEP += i
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um número inteiro válido. \033[m")
            continue
        except (KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número. \033[m")
            return 0
        finally:
            return strCEP

    
def linha(tam = 139):
    return "\033[35m\033[1m⁃\033[0;0m" * tam

def cabecalho(txt):
    print(linha())
    print(f"\033[36m\033[1m{txt.center(130)}\033[0;0m")
    print(linha())

def menu(lista, titulo):
    cabecalho(f"\033[36m{titulo.center(130)}\033[0;0m")
    c = 1
    for item in lista:
        print(f"\033[1m\033[36m{c} - \033[0;0m\033[35m{item}\033[m")
        c += 1
    print(linha())
    opc = leiaInt("\033[36m\033[1mSua opção: \033[35m")
    return opc
