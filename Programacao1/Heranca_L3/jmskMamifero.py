from jmskAnimal import Animal

class Mamifero(Animal):
    def __init__(self, nome, dataNascimento, habitat, especie, peso, alimentacao, qtdMamas):
        super().__init__(nome, dataNascimento, habitat, especie, peso, alimentacao)
        self.__qtdMamas = qtdMamas

    def fazerSom(self):
        return "Meow"
    
    def amamentar(self):
        return "Amamentando"
    
    def __str__(self): 
        return str(super().__str__()) + "\nQuantidade de Mamas: " + str(self.__qtdMamas)
    
    @property
    def qtdMamas(self):
        return self.__qtdMamas
    
    @qtdMamas.setter
    def alteraqtdMamas(self, novaqtdMamas):
        self.__qtdMamas = novaqtdMamas