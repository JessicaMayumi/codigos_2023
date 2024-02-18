class ContaBancaria:
    def __init__(self,titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, valor):
        self.saldo = float(self.saldo) + float (valor)

    def sacar(self,valor):
        if self.saldo >= valor:
            self.saldo = float (self.saldo) - float (valor)

    def apresentar(self):
        return ("Titular: " + self.titular + "\nSaldo: R$ %.2f" %float(self.saldo))

def exibe_menu():
    print("\nDigite a opcao desejada:")
    print("1: Depositar")
    print("2: Sacar")
    print("3: Consultar")
    print("x: Sair")

nomeTitular = input("Insira seu nome: ")
pessoa1 = ContaBancaria(nomeTitular)

resposta = "1"
while resposta.upper != "X":
    exibe_menu()
    resposta = input()

    # 1: depositar
    if resposta == "1":
        valorDepositar = float(input("Insira um valor a depositar: "))
        pessoa1.depositar(valorDepositar)
    elif resposta == "2":
        valorSacar = float(input("Insira um valor para sacar: "))
        pessoa1.sacar(valorSacar)
    elif resposta == "3":
        pessoa1
    # fazer o procedimento correspondente
    print(pessoa1.apresentar())










'''

pergunta_depositar = input("Deseja depositar algum valor? (S ou N): ")
if pergunta_depositar.upper() == "S":
    valorDepositar = float(input("Insira um valor a depositar: "))
    pessoa1.depositar(valorDepositar)

pergunta_sacar = input("Deseja sacar algum valor? (S ou N): ")
if pergunta_sacar.upper() == "S":
    valorSacar = float(input("Insira um valor para sacar: "))
    pessoa1.sacar(valorSacar)

consultar_saldo = input ("Deseja consultar seu saldo? (S ou N): ")
if consultar_saldo.upper() == "S":
    pessoa1
            
print(pessoa1.apresentar())

'''