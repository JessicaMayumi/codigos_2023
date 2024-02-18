from Interface import *
from Arquivos import *
from time import sleep
from Restaurante import *

arquivo = "restaurantes.txt"
lista = []

if not verificarArquivo(arquivo):
    criarArquivo(arquivo)
else: 
    lista = lerArquivo(arquivo)

cabecalho("⊳  ⊳  ⊳  Cadastro de Restaurantes  ⊲  ⊲  ⊲")
while True:
    resposta = menu(["Cadastrar Restaurante", "Alterar dados do Restaurante", "Excluir Restaurante","Listar Restaurante", "Sobre o sistema", "Sair do Sistema"], "Menu Principal")
    # resposta = menu(["Listar Restaurantes", "Cadastrar Restaurante","Sair do Sistema"])
    if resposta == 1:
        cabecalho("Novo Cadastro")
        nome = str(input("\033[36m\033[1mNome: \033[0;0m\033[35m"))
        endereco = str(input("\033[36m\033[1mEndereço: \033[0;0m\033[35m"))
        telefone = VerificarTelefone("\033[36m\033[1mTelefone: \033[0;0m\033[35m")
        cep = VerificarCEP("\033[36m\033[1mCEP: \033[0;0m\033[35m")
        nota = leiaIntNota("\033[36m\033[1mNota: \033[0;0m\033[35m")
        restaurante = Restaurante(nome.upper(), endereco, telefone, cep, nota)
        lista.append(restaurante)
        cadastrar(arquivo, lista)

    elif resposta == 2:
        cabecalho("Alterar Dados")
        vazio = ""
        print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<26}\033[1;36m| \033[34m‣ Telefone{vazio:<5}\033[1;36m| \033[34m‣ CEP{vazio:<5}\033[1;36m| \033[34m‣ Nota{vazio:<10}\033[1;36m| \033[34m‣ Endereço{vazio:<49}\033[1;36m|\033[0;0m")
        for item in lista:
            index = lista.index(item)
            if (index % 2) == 1:
                print(f"\033[46m\033[35m{item.imprimirLado()}\033[0;0m")
            else:
                print(f"\033[35m{item.imprimirLado()}\033[0;0m")
        procurarNome = input("\n\033[35m\033[1mInsira CORRETAMENTE o NOME do RESTAURANTE  na qual você deseja alterar os dados: \033[36m")
        achados = []
        for item in lista:
            if item.nome.upper() == procurarNome.upper():
                res = item
                achados.append(res)
        if len(achados) == 0:
            print("Restaurante inválido! ")
        elif len(achados) == 1:
            altDados = menu(["Nome", "Endereço", "Telefone", "CEP", "Nota"], "Selecione o que você deseja alterar!")
            if altDados == 1:
                novoNome = input(f"\033[36m\033[1mInsira o novo NOME para '{res.nome}': \033[35m")
                res.nome = novoNome
            elif altDados == 2: 
                novoEndereco = input("\033[36m\033[1mInsira o novo ENDEREÇO: \033[35m")
                res.endereco = novoEndereco
            elif altDados == 3:
                novoTelefone = VerificarTelefone("\033[36m\033[1mInsira o novo TELEFONE: \033[35m")
                res.telefone = novoTelefone
            elif altDados == 4:
                novoCep = VerificarCEP("\033[36m\033[1mInsira o novo CEP: \033[35m")
                res.cep = novoCep
            elif altDados == 5:
                novaNota = leiaIntNota("\033[36m\033[1mInsira a nova NOTA: \033[35m")
                res.nota = novaNota
            else: 
                print("\033[31mErrro! Digite uma opção válida!\033[m")
            alterar(arquivo, lista, res)
        else:
            achados.append("Nenhum dos Anteriores")
            excRestaurante = menu(achados, "Selecione o Restaurante que você deseja EXCLUIR!")
            if excRestaurante != len(achados):
                for i in range(len(achados)):
                    res = achados[i]
                    resAchados = input(f"\033[35m\033[1mRealmente deseja alterar os dados do Restaurante {res.nome}? (S ou N): \033[36m")
                    if resAchados.upper() == "S":
                        altDados = menu(["Nome", "Endereço", "Telefone", "CEP", "Nota"], "Selecione o que você deseja alterar!")
                        if altDados == 1:
                            novoNome = input(f"\033[0;0m\033[35mInsira o novo NOME para '{res.nome}': \033[36m")
                            res.nome = novoNome
                        elif altDados == 2: 
                            novoEndereco = input(f"\033[0;0m\033[35mInsira o novo ENDEREÇO para '{res.nome}': \033[36m")
                            res.endereco = novoEndereco
                        elif altDados == 3:
                            novoTelefone = VerificarTelefone(f"\033[0;0m\033[35mInsira o novo TELEFONE para '{res.nome}': \033[36m")
                            res.telefone = novoTelefone
                        elif altDados == 4:
                            novoCep = VerificarCEP(f"\033[0;0m\033[35mInsira o novo CEP para '{res.nome}': \033[36m")
                            res.cep = novoCep
                        elif altDados == 5:
                            novaNota = leiaIntNota(f"\033[0;0m\033[35mInsira a nova NOTA para '{res.nome}': \033[36m")
                            res.nota = novaNota
                        else: 
                            print("\033[31mErrro! Digite uma opção válida!\033[m")
                        alterar(arquivo, lista, res)
                        break
                    elif resAchados.upper() == "N":
                        break
                    else:
                        print("\033[31mERRO! Insira apenas S ou N!\033[m")
        
    elif resposta == 3:
        procurarNome = input("\n\033[35m\033[1mInsira CORRETAMENTE o NOME do RESTAURANTE  na qual você deseja excluir TODOS os dados: \033[36m")
        achados = []
        vazio = ""
        for item in lista:
            if item.nome.upper() == procurarNome.upper():
                res = item
                achados.append(res)
        if len(achados) == 0:
            print("Restaurante não encontrado! ")
        elif len(achados) == 1:
            # resAchados = input(f"Realmente deseja excluir TODOS os dados do seguinte restaurante?\n\033[1m\033[41m| Nome{vazio:<26}| Telefone{vazio:<4}| CEP{vazio:<6}| Nota{vazio:<5}| Endereço{vazio:<51}|\033[0;0m\n{achados[0].imprimirLado()}\n(S ou N): ")
            resAchados = input(f"\033[35m\033[1mRealmente deseja excluir TODOS os dados do Restaurante {res.nome}? (S ou N): \033[36m")
            if resAchados.upper() == "S":
                print(f"\033[31m\033[1mRestaurante {res.nome} EXCLUIDO!\033[m")
                lista.remove(achados[0])
            elif resAchados.upper() == "N":
                pass
            else:
                print("\033[31mERRO! Insira apenas S ou N!\033[m")
        else:
            achados.append("Nenhum dos Anteriores")
            excRestaurante = menu(achados, "Selecione o Restaurante que você deseja EXCLUIR!")
            if excRestaurante != len(achados):
                for i in range(len(achados)):
                    res = achados[i]
                    resAchados = input(f"\033[35m\033[1mRealmente deseja excluir TODOS os dados do Restaurante {res.nome}? (S ou N): \033[m")
                    if resAchados.upper() == "S":
                        lista.remove(achados[i])
                        print(f"\033[31mRestaurante {res.nome} EXCLUIDO!\033[m")
                        break
                #if excRestaurante == 1:
            #    resAchados = input(f"Realmente deseja excluir TODOS os dados do Restaurante {res.nome}? (S ou N): ")
            #    if resAchados.upper() == "S":
            #        lista.remove[achados[excRestaurante-1]]
                
    elif resposta == 4:
        cabecalho("Listando Restaurantes")
        vazio = ""
        print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<26}\033[1;36m| \033[34m‣ Telefone{vazio:<5}\033[1;36m| \033[34m‣ CEP{vazio:<5}\033[1;36m| \033[34m‣ Nota{vazio:<10}\033[1;36m| \033[34m‣ Endereço{vazio:<49}\033[1;36m|\033[0;0m")
        for item in lista:
            index = lista.index(item)
            if (index % 2) == 1:
                print(f"\033[46m\033[35m{item.imprimirLado()}\033[0;0m")
            else:
                print(f"\033[35m{item.imprimirLado()}\033[0;0m")
            

    elif resposta == 5:
        cabecalho("Créditos")
        print("\033[35mEste sistema foi construído em Python, utilizando conhecimentos básicos de guardar dados em arquivos.\nDesenvolvido nas residências do Instituto Federal Catarinense - Campus Blumenau\nDesenvolver(a): Jessica Mayumi Schuhmacher Kogake | 201 informática \033[m")

    elif resposta == 6:
        print("\033[35m\033[1mSaindo do sistema... Até logo! \033[m")
        break
    
    else:
        print("\033[31mErrro! Digite uma opção válida!\033[m")
    sleep(2)

# FORMATACAO DE TELEFONE
# VERIFICAR CASO JA TENHA UM REGISTRO COM TODOS OS CAMPOS IGUAIS