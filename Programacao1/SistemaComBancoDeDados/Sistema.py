from Interface import *
from time import sleep
from Funcionario import *
from Restaurante import *
from datetime import datetime
from VerificarCPF import *

from RestauranteDAO import RestauranteDAO
from FuncionarioDAO import FuncionarioDAO

restauranteDAO = RestauranteDAO()
funcionarioDAO = FuncionarioDAO()

cabecalho("⊳  ⊳  ⊳  Cadastro de Restaurantes  ⊲  ⊲  ⊲")
while True:
    resposta = menu(["Cadastrar Restaurante", "Alterar dados do Restaurante", "Excluir Restaurante","Listar Restaurante", "Acesso Restrito", "Sobre o sistema", "Sair do Sistema"], "Menu Principal")
    # resposta = menu(["Listar Restaurantes", "Cadastrar Restaurante","Sair do Sistema"])
    if resposta == 1:
        cabecalho("Novo Cadastro")
        nome = str(input("\033[36m\033[1mNome: \033[0;0m\033[35m"))
        endereco = str(input("\033[36m\033[1mEndereço: \033[0;0m\033[35m"))
        telefone = VerificarTelefone("\033[36m\033[1mTelefone: \033[0;0m\033[35m")
        cep = VerificarCEP("\033[36m\033[1mCEP: \033[0;0m\033[35m")
        nota = leiaIntNota("\033[36m\033[1mNota: \033[0;0m\033[35m")
        restaurante = Restaurante(nome.upper(), endereco, telefone, cep, nota)
        if restauranteDAO.insereRestaurante(restaurante):
            print(f"\033[32m\033[1mO Restaurante {restaurante.nome.upper()} foi adicionado com sucesso!\033[0;0m")

    elif resposta == 2:
        cabecalho("Alterar Dados")
        vazio = ""
        print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<20}\033[1;36m| \033[34m‣ Telefone{vazio:<5}\033[1;36m| \033[34m‣ CEP{vazio:<5}\033[1;36m| \033[34m‣ Nota{vazio:<10}\033[1;36m| \033[34m‣ Endereço{vazio:<40}\033[1;36m| \033[34m‣ ID{vazio:<5}\033[1;36m|\033[0;0m")
        for item in restauranteDAO.buscaRestaurantes():
            contador = 0
            if contador % 2 == 1:
                print(f"\033[46m\033[35m{item.imprimirLado()}\033[0;0m")
            else:
                print(f"\033[35m{item.imprimirLado()}\033[0;0m")
            contador+=1
        procurarID = input("\n\033[35m\033[1mInsira o ID do RESTAURANTE  na qual você deseja alterar os dados: \033[36m")
        if restauranteDAO.buscaRestaurante(procurarID) == None:
            print("ID inválido! ")
        else:
            res = restauranteDAO.buscaRestaurante(procurarID)
            altDados = menu(["Nome", "Endereço", "Telefone", "CEP", "Nota"], "Selecione o que você deseja alterar!")
            if altDados == 1:
                novoNome = input(f"\033[36m\033[1mInsira o novo NOME para '{res.nome}': \033[35m")
                res.nome = novoNome.upper()
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
            confirmacao = input(f"\033[35m\033[1mRealmente deseja alterar os dados do Restaurante {res.nome}? (S ou N): \033[36m")    
            if confirmacao.upper() == "S":
                print(f"\033[32m\033[1mRestaurante {res.nome} alterado!\033[m")
                restauranteDAO.alteraRestaurante(res)
            elif confirmacao.upper() == "N":
                pass
            else:
                print("\033[31mERRO! Insira apenas S ou N!\033[m")
        
    elif resposta == 3:
        print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<20}\033[1;36m| \033[34m‣ Telefone{vazio:<5}\033[1;36m| \033[34m‣ CEP{vazio:<5}\033[1;36m| \033[34m‣ Nota{vazio:<10}\033[1;36m| \033[34m‣ Endereço{vazio:<40}\033[1;36m| \033[34m‣ ID{vazio:<5}\033[1;36m|\033[0;0m")
        for item in restauranteDAO.buscaRestaurantes():
            print(item.imprimirLado())
        procurarID = input("\n\033[35m\033[1mInsira o ID do RESTAURANTE  na qual você deseja excluir TODOS os dados: \033[36m")
        vazio = ""
        if restauranteDAO.buscaRestaurante(procurarID) == None:
            print("Restaurante não encontrado! ")
        else:
            res = restauranteDAO.buscaRestaurante(procurarID)
            # resAchados = input(f"Realmente deseja excluir TODOS os dados do seguinte restaurante?\n\033[1m\033[41m| Nome{vazio:<26}| Telefone{vazio:<4}| CEP{vazio:<6}| Nota{vazio:<5}| Endereço{vazio:<51}|\033[0;0m\n{achados[0].imprimirLado()}\n(S ou N): ")
            confirmacao = input(f"\033[35m\033[1mRealmente deseja excluir TODOS os dados do Restaurante {res.nome}? (S ou N): \033[36m")
            if confirmacao.upper() == "S":
                print(f"\033[31m\033[1mRestaurante {res.nome} EXCLUIDO!\033[m")
                restauranteDAO.apagarRestaurante(res)
            elif confirmacao.upper() == "N":
                pass
            else:
                print("\033[31mERRO! Insira apenas S ou N!\033[m")
# # 
#                 if excRestaurante == 1:
            #    resAchados = input(f"Realmente deseja excluir TODOS os dados do Restaurante {res.nome}? (S ou N): ")
            #    if resAchados.upper() == "S":
                #    lista.remove[achados[excRestaurante-1]]
                
    elif resposta == 4:
        cabecalho("Listando Restaurantes")
        vazio = ""
        print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<20}\033[1;36m| \033[34m‣ Telefone{vazio:<5}\033[1;36m| \033[34m‣ CEP{vazio:<5}\033[1;36m| \033[34m‣ Nota{vazio:<10}\033[1;36m| \033[34m‣ Endereço{vazio:<40}\033[1;36m| \033[34m‣ ID{vazio:<5}\033[1;36m|\033[0;0m")
        
        for item in restauranteDAO.buscaRestaurantes():
            print(item.imprimirLado())
            # contador = 0
            # if contador % 2 == 1:
            #     print(f"\033[46m\033[35m{item.imprimirLado()}\033[0;0m")
            # else:
            #     print(f"\033[35m{item.imprimirLado()}\033[0;0m")
            # contador+=1
            
    elif resposta == 5:
        senha = input("\033[36mInsira a Senha: \033[35m")
        if int(senha) != 12345:
            print("\033[31mSenha Incorreta! Boa sorte da próxima vez :)\033[0;0m")
        else:
            print("\033[32mAcesso Autorizado!\033[0;0m")
            menuFunc = menu(["Cadastrar Funcionário", "Alterar Dados", "Listar Funcionários", "Excluir Dados", "Voltar ao Início"], "Acesso Restrito")
            if menuFunc == 1:
                restauranteDAO = RestauranteDAO()
                cabecalho("Novo Cadastro")
                nome = str(input("\033[36m\033[1mNome: \033[0;0m\033[35m"))
                cargo = str(input("\033[36m\033[1mCargo: \033[0;0m\033[35m"))
                salario = float(input("\033[36m\033[1mSalário: \033[0;0m\033[35m"))
                cpf = VerificarCPF("\033[36m\033[1mCPF (xxx.xxx.xxx-xx) : \033[0;0m\033[35m")
                dataContratacao = input("\033[36m\033[1mData de Contratação (DD/MM/AA): \033[0;0m\033[35m")
                restaurante = input("\033[36m\033[1mInsira o nome do Restaurante: \033[0;0m\033[35m")
                while True:
                    if restauranteDAO.buscaRestauranteNome(restaurante) == None:
                        print("\033[31mRestaurante não encontrado!\033[m")
                        restaurante = input("\033[36m\033[1mInsira o nome do Restaurante: \033[0;0m\033[35m")
                    else:
                        restaurante = restauranteDAO.buscaRestauranteNome(restaurante)
                        break
                funcionario = Funcionario(nome.upper(), cargo, salario, cpf, dataContratacao, restaurante.id)
                if funcionarioDAO.insereFuncionario(funcionario):
                    print(f"\033[32m\033[1mO Funcionário(a) {funcionario.nome.upper()} foi adicionado com sucesso!\033[0;0m")

            elif menuFunc == 2:
                cabecalho("Alterar Dados")
                vazio = ""
                print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<26}\033[1;36m| \033[34m‣ Cargo{vazio:<9}\033[1;36m| \033[34m‣ Salário{vazio:<2}\033[1;36m| \033[34m‣ CPF{vazio:<11}\033[1;36m| \033[34m‣ Contratação{vazio:<1}\033[1;36m| \033[34m‣ Nome do Restaurante{vazio:<16}\033[1;36m|\033[0;0m")
                #print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<26}\033[1;36m| \033[34m‣ Telefone{vazio:<5}\033[1;36m| \033[34m‣ CEP{vazio:<5}\033[1;36m| \033[34m‣ Nota{vazio:<10}\033[1;36m| \033[34m‣ Endereço{vazio:<49}\033[1;36m|\033[0;0m")
                for item in funcionarioDAO.buscaFuncionarios():
                    print(item.imprimirLado())
                procurarID = input("\n\033[35m\033[1mInsira o CPF do Funcionário na qual você deseja alterar os dados: \033[36m")
                if funcionarioDAO.buscaFuncionario(procurarID) == None:
                    print("\033[31mCPF inválido! \033[m")
                else:
                    func = funcionarioDAO.buscaFuncionario(procurarID)
                    altDados = menu(["Nome", "Cargo", "Salario"], "Selecione o que você deseja alterar!")
                    if altDados == 1:
                        novoNome = input(f"\033[36m\033[1mInsira o novo NOME para '{func.nome}': \033[35m")
                        func.nome = novoNome
                    elif altDados == 2: 
                        novoCargo = input("\033[36m\033[1mInsira o novo CARGO: \033[35m")
                        func.cargo = novoCargo
                    elif altDados == 3:
                        novoSalario = float(input("\033[36m\033[1mInsira o novo SALÁRIO: \033[35m"))
                        func.salario = novoSalario
                    else: 
                        print("\033[31mErrro! Digite uma opção válida!\033[m")
                    if funcionarioDAO.alteraFuncionario(func):
                        print(f"\033[32m\033[1mDados do funcionário(a) {func.nome.upper()} foi altrados com sucesso!\033[0;0m")
            elif menuFunc == 4:
                vazio = ""
                print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<26}\033[1;36m| \033[34m‣ Cargo{vazio:<9}\033[1;36m| \033[34m‣ Salário{vazio:<2}\033[1;36m| \033[34m‣ CPF{vazio:<11}\033[1;36m| \033[34m‣ Contratação{vazio:<1}\033[1;36m| \033[34m‣ Nome do Restaurante{vazio:<16}\033[1;36m|\033[0;0m")
                for item in funcionarioDAO.buscaFuncionarios():
                    print(item.imprimirLado())
                procurarCPF = input("\n\033[35m\033[1mInsira o CPF do Funcionário na qual você deseja excluir TODOS os dados: \033[36m")
                vazio = ""
                if funcionarioDAO.buscaFuncionario(procurarCPF) == None:
                    print("\033[31mO CPf inserido está inválido ou não está cadastrado! \033[m")
                    pass
                else:
                    func = funcionarioDAO.buscaFuncionario(procurarCPF)
                    # resAchados = input(f"Realmente deseja excluir TODOS os dados do seguinte restaurante?\n\033[1m\033[41m| Nome{vazio:<26}| Telefone{vazio:<4}| CEP{vazio:<6}| Nota{vazio:<5}| Endereço{vazio:<51}|\033[0;0m\n{achados[0].imprimirLado()}\n(S ou N): ")
                    confirmacao = input(f"\033[35m\033[1mRealmente deseja excluir TODOS os dados do Funcionários {func.nome}? (S ou N): \033[36m")
                    if confirmacao.upper() == "S":
                        print(f"\033[31m\033[1mFuncionário {func.nome} EXCLUÍDO!\033[m")
                        funcionarioDAO.apagarFuncionario(func)
                    elif confirmacao.upper() == "N":
                        pass
                    else:
                        print("\033[31mERRO! Insira apenas S ou N!\033[m")                    
            elif menuFunc == 3:
                cabecalho("Listando Funcionário")
                vazio = ""
                print(f"\033[46m\033[1m| \033[34m‣ Nome{vazio:<26}\033[1;36m| \033[34m‣ Cargo{vazio:<9}\033[1;36m| \033[34m‣ Salário{vazio:<2}\033[1;36m| \033[34m‣ CPF{vazio:<11}\033[1;36m| \033[34m‣ Contratação{vazio:<1}\033[1;36m| \033[34m‣ Nome do Restaurante{vazio:<16}\033[1;36m|\033[0;0m")
                for item in funcionarioDAO.buscaFuncionarios():
                    print(item.imprimirLado())

            elif menuFunc == 5:   
                continue

            else:
                print("\033[31mErrro! Digite uma opção válida!\033[m")

    elif resposta == 6:
        cabecalho("Créditos")
        print("\033[35mEste sistema foi construído em Python, utilizando conhecimentos básicos de armazenar Dados em um Banco de Dados(MySQL).\nDesenvolvido nas residências do Instituto Federal Catarinense - Campus Blumenau\nDesenvolver(a): Jessica Mayumi Schuhmacher Kogake | 201 informática | 2023\033[m")

    elif resposta == 7:
        print("\033[35m\033[1mSaindo do sistema... Até logo! \033[m")
        break
    
    else:
        print("\033[31mErrro! Digite uma opção válida!\033[m")
    sleep(2)
