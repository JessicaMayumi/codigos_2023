class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return "Nome: "+ str(self.nome)+ "\nIdade: " + str(self.idade)

n = "Mayumi"
i= 16

pessoa1 = Pessoa(n,i)

print(pessoa1.apresentar())
