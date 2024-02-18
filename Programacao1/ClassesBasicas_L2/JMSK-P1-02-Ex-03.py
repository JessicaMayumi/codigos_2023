class ContaBancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = float(self.saldo) + float (valor)

    def sacar(self,valor):
        self.saldo = float (self.saldo) - float (valor)

    def apresentar(self):
        return ("Titular: " + self.titular + "\nSaldo: R$ %.2f" %float(self.saldo))
    

nomeTitular = input("Insira seu nome: ")
saldoBancario = input("Insira seu saldo atual: ")

pessoa1 = ContaBancaria(nomeTitular,saldoBancario)

pergunta_depositar = input("Deseja depositar algum valor? (S ou N): ")
if pergunta_depositar.upper() == "S":
    valorDepositar = float(input("Insira um valor a depositar: "))
    pessoa1.depositar(valorDepositar)

pergunta_sacar = input("Deseja depositar algum valor? (S ou N): ")
if pergunta_sacar.upper() == "S":
    valorSacar = float(input("Insira um valor para sacar: "))
    pessoa1.sacar(valorSacar)

consultar_saldo = input ("Deseja consultar seu saldo? (S ou N): ")
if consultar_saldo.upper() == "S":
    pessoa1
            
print(pessoa1.apresentar())