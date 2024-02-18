from jmskAnimal import Animal

class Ave(Animal):
    def __init__(self,nome, dataNascimento, habitat, especie, peso, alimentacao, qtdAsas, tipoBico):
        super().__init__(nome, dataNascimento, habitat, especie, peso, alimentacao)
        self.__qtdAsas = qtdAsas 
        self.__tipoBico = tipoBico

    def fazerSom(self):
        return "Quack"
    
    def voar(self):
        return ("voando")
    
    def __str__(self):
        return str(super().__str__()) + "\nQuantidade de Asas: " + str(self.__qtdAsas) + "\nTipo de Bico: " + str(self.__tipoBico)
    
    @property
    def qtdAsas(self):
        return self.__qtdAsas
    
    @property
    def tipoBico(self):
        return self.__tipoBico
    
        
    @qtdAsas.setter
    def alteraqtdAsas(self, novaqtdAsas):
        self.__qtdAsas = novaqtdAsas

    @tipoBico.setter
    def alteratipoBico(self, novatipoBico):
        self.__tipoBico = novatipoBico

