from Cliente import Cliente
from ContaCorrent import ContaCorrente

listaConta = []
print("Cadastro de Clientes")
nome = input("Insira seu nome: ")
cpf = input("Insira seu CPF: ")
perguntaSaldo = input ("Deseja inserir algum valor na conta?(S ou N):")
if perguntaSaldo.upper() == "S":
    saldo = float(input("Insira o valor: "))
cliente = Cliente(nome, cpf)
conta = ContaCorrente(len(listaConta), saldo, cliente)
listaConta.append(conta)
maior = listaConta[0]
menor = listaConta[0]


while True:
    pergunta = input("Deseja cadastrar um novo cliente?(S ou N) ")
    if pergunta.upper() == "N":
        break
    if pergunta.upper() == "S":
        nome = input("Insira seu nome: ")
        cpf = input("Insira seu CPF: ")
        perguntaSaldo = input ("Deseja inserir algum valor na conta?(S ou N):")
        if perguntaSaldo.upper() == "S":
            saldo = float(input("Insira o valor: "))
        else:
            saldo = 0.00
        cliente = Cliente(nome, cpf)
        conta = ContaCorrente(len(listaConta), saldo, cliente)
        listaConta.append(conta)
        if saldo > maior.saldoInicial:
            maior = conta
        if saldo < menor.saldoInicial:
            menor = conta

for cliente in listaConta:
    print(f"Número da Conta: {cliente.numero}\nSaldo: {cliente.saldoInicial}")

print (f"\n- Maior conta: \n{maior}")
print(f"\n-Menor conta: \n{menor}")




