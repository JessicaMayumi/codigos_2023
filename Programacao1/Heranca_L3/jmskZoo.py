from jmskAnimal import Animal
from jmskMamifero import Mamifero
from jmskAve import Ave
from jmskReptil import Reptil

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionarAnimal(self, animal):
        self.animais.append(animal)

    def listaAnimal(self, nome): #apresentar o animal pelo nome
        for animal in self.animais:
            if str(nome).upper() == animal.nome:
                return animal

    def transferirAnimal(self, animal):
        self.animais.remove(animal)

    def listaTodosAnimais(self):
        strAnimais = ""
        for animal in self.animais:
            strAnimais = str(animal) + "\n"
            return strAnimais

    def listarEspecie(self, especie):
        for animal in self.animais:
            if str(especie).upper() == animal.especie:
                return animal

    def listarAnimaisPeloAnoNascimento(self, ano): #apresentar o animal pelo ano
        for animal in self.animais:
            if str(ano).upper() == animal.ano:
                return animal