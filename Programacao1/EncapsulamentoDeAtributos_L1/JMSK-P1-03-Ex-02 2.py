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
    def nome(self):
        return self.__nome
    
    @property
    def numeroEleitor(self):
        return self.__numeroEleitor
    
    #Metodo imprimir, para poder imprimir os dados do objeto
    def imprimir(self):
        return "Nome: " + str(self.__nome) + "\n\tNúmero: " + str(self.__numeroEleitor) + "\n\tIdade: " + str(self.__idade)

#cadastro
dados = []

print ("Cadastre-se")
nome = input("Insira o nome: ")
numero = input("Insira o número de eleitor: (xxx-x) ")
idade = int(input("Insira a idade: "))        
dados.append( Eleitor(nome, idade, numero) )
soma = dados[0].idade

mais_novo = dados[0]
mais_velho = dados[0]

# entrada de dados
while True:
    pergunta = input("Deseja cadastrar um novo eleitor? ( S / N ): ")
    if pergunta.upper() == "N":
        break
    if pergunta.upper() == "S":
        nome = input("Insira o nome: ")
        numero = input("Insira o número de eleitor: (xxx-x) ")
        idade = int(input("Insira a idade: "))       
        um_eleitor =  Eleitor(nome, int(idade), numero) 
        dados.append( um_eleitor )
        soma += idade
        if um_eleitor.idade < mais_novo.idade:    
                mais_novo = um_eleitor
        if um_eleitor.idade > mais_novo.idade:
                mais_velho = um_eleitor
        
# calculo da media, depois de ter todos os eleitores na lista
media = soma/len(dados)

#verificar quantos eleitores estao acima da média das idades
acima_da_media = 0
for eleitor in dados:
    if eleitor.idade > media:
        acima_da_media += 1

print ("Média das idades: {} anos." .format(media) )
print ("Quantidade de eleitores que possuem idade acima da média: ", acima_da_media)
print (f"Eleitor mais novo: \n\t{mais_novo.imprimir()} \nEleitor mais velho: \n\t{mais_velho.imprimir()}")        
        