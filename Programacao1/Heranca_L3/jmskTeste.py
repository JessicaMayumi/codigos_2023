from jmskZoo import Zoologico
from jmskAnimal import Animal
from jmskMamifero import Mamifero
from jmskAve import Ave
from jmskReptil import Reptil

zoo = Zoologico()

while True:
    pergunta = input("Deseja inserir um animal ao Zoo? ( 'S'  ou  'N' ): ")
    if pergunta.upper() == "N":
        break
    if pergunta.upper() == "S":
        nome = input("Insira o nome do Animal: ")
        dataNascimento = input("Insira a Data de Nascimento do Animal: ")
        habitat = input("Insira o Habitat do Animal: ")
        peso = input("Insira o Peso do Animal: ")
        alimentacao = input("Insira a Alimentação do Animal: ")
        #-------------------------------------------------------------------
        print("Insira a Espécie do Animal:")
        pergunta_especie = int(input("1 - Mamífero\n2 - Ave\n3 - Réptil\n "))
        if pergunta_especie == 1:
            especie = "Mamífero"
        elif pergunta_especie == 2:
            especie = "Ave"
        elif pergunta_especie == 3:
            especie = "Réptil"
        else:
            especie = "Espécie não identificada!"
        #-------------------------------------------------------------------
        animal = Animal(nome, dataNascimento, habitat, especie, peso, alimentacao)
        if especie == "Mamífero":
            qtdMamas = int(input("Insira a quantidade de Mamas: "))
            animal = Mamifero(nome, dataNascimento, habitat, especie, peso, alimentacao, qtdMamas)
        elif especie == "Ave":
            qtdAsas = int(input("Insira a Quantidade de asas: "))
            tipoBico = input("Insira o Tipo de Bico: ")
            animal = Ave(nome, dataNascimento, habitat, especie, peso, alimentacao, qtdAsas, tipoBico)
        elif especie == "Réptil":
            temperaturaCorpo = int(input("Insira a Temperatura do Corpo: "))
            pele = input("Insira a pele do Animal: ")
            animal = Reptil(nome, dataNascimento, habitat, especie, peso, alimentacao, temperaturaCorpo, pele)
        zoo.adicionarAnimal(animal)
        
        

print(zoo.listaTodosAnimais())
        


