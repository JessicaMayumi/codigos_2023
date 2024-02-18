from jmskAnimal import Animal

class Reptil(Animal):
    def __init__(self, nome, dataNascimento, habitat, especie, peso, alimentacao, temperaturaCorpo, pele):
        super().__init__(nome, dataNascimento, habitat, especie, peso, alimentacao)
        self.__temperaturaCorpo = temperaturaCorpo
        self.__pele = pele

    def fazerSom(self):
        return "Rabit"
    
    def regularTemperatura(self):
        return "Regulando Temperatura"
    
    def __str__(self):
        return str(super().__str__()) + "\nTemperatura do Corpo: " + str(self.__temperaturaCorpo) + "\nPele: " + self.__pele
    
    
    @property
    def temperaturaCorpo(self):
        return self.__temperaturaCorpo
    
    @property
    def pele(self):
        return self.__pele
    
    @temperaturaCorpo.setter
    def alteraTemperaturaCorpo(self, novaTemperaturaCorpo):
        self.__temperaturaCorpo = novaTemperaturaCorpo

    @pele.setter
    def alteraPele(self, novaPele):
        self.__pele = novaPele