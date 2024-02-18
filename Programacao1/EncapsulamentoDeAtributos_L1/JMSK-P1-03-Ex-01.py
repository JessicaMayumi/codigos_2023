class Eleitor:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    
    def verificar(self):
        if self.__idade < 16:
            return self.__nome + "ainda não pode votar. Tem apenas" + str(self.__idade) + "anos."
        elif self.__idade >= 18 and self.__idade <= 65:
            return self. __nome + " - " + str(self.__idade) + " anos deve votar."
        else:
            return self.__nome + " - " + str(self.__idade) + " anos, Voto facultativo."
    
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self,nova_idade):
        self.__idade = nova_idade


nome = input("Insira seu nome: ")
idade = int( input("Insira sua idade: ") )

e1 = Eleitor(nome,idade)
print(e1.verificar())

nova_idade = int(input("Insira sua nova idade: "))
e1.idade = nova_idade
print(e1.verificar())
