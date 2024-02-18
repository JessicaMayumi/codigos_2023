class Eleitor:
    def __init__(self, nome, idade, numeroEleitor):
        self.__nome = nome
        self.__idade = idade
        self.__numeroEleitor = numeroEleitor
    
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
    
    @property
    def numeroEleitor(self):
        return self.__numeroEleitor

    @idade.setter
    def idade(self,nova_idade):
        self.__idade = nova_idade

#cadastro
dados = []
while True:
    pergunta = input("Deseja cadastrar um novo eleitor? ( S / N ): ")
    if pergunta.upper == "N":
        break
    else:
        nome = input("Insira o nome: ")
        numero = input("Insira o número de eleitor: (xxx-x) ")
        idade = int(input("Insira a idade: "))        
        for i in range(len(dados)):
            dados.append( Eleitor(nome, numero, idade) )
