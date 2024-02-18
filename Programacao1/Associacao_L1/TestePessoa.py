from Endereco import Endereco
from Pessoa import Pessoa

listaPessoa = []
soma = 0

while True:
    resposta = input("Deseja inserir um endereço?( S ou N ): ")
    if resposta.upper() == "N":
        break
    if resposta.upper() == "S":
        nome = input("Insira o nome: ")
        idade = int(input("Insira a idade: "))
        rua = input("Insira a rua: ")
        numero = int(input("Insria o número da casa: "))
        bairro = input("Insira o bairro: ")
        cidade = input("Insira a cidade: ")
        cep = input("Insira o CEP: ")
        end = Endereco(rua, numero, bairro, cidade, cep)
        pes = Pessoa(nome, idade, end)
        listaPessoa.append(pes)
        soma += idade 

media = soma/len(listaPessoa)
print("Média das idades das pessoas cadastradas: ", media)
for pessoa in listaPessoa:
    print(pessoa, "\n")



while True:
    numero_de_pessoas = 0
    perguntar_cidade = input("Insira o nome de uma cidade (enter para parar): ")
    if perguntar_cidade == "":
        break
    else:
        for pessoa in listaPessoa:
            if perguntar_cidade.upper() == pessoa.endereco.cidade.upper():
                numero_de_pessoas += 1
        print(f"O número de pessoas cadastradas em {perguntar_cidade.upper()} é {numero_de_pessoas}.")
