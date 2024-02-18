import abc
class Animal(abc.ABC):
    def __init__(self, nome, dataNascimento, habitat, especie, peso, alimentacao):
        self.__nome = nome
        self.__dataNascimento = dataNascimento
        self.__habitat = habitat
        self.__especie = especie
        self.__peso = peso
        self.__alimentacao = alimentacao

    def fazerSom(self):
        pass

    def __str__(self):
        return "Nome: " + self.__nome + "\nData de Nascimento: " + str(self.__dataNascimento) + "\nHabitat: " + self.__habitat + "\nEspécie: " + self.__especie + "\nPeso: " + str(self.__peso) + "\nAlimentação: " + self.__alimentacao
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    
    @property
    def habitat(self):
        return self.__habitat
    
    @property
    def especie(self):
        return self.__especie
    
    @property 
    def peso(self):
        return self.__peso
    
    @property
    def alimentacao(self):
        return self.__alimentacao
    
    @nome.setter
    def alteraNome(self, novoNome):
        self.__nome = novoNome

    @dataNascimento.setter
    def alteraDataNascimento(self, novaData):
        self.__dataNascimento = novaData

    @habitat.setter
    def alteraHabitat(self, novoHabitat):
        self.__habitat = novoHabitat

    @especie.setter
    def alteraEspecie(self, novaEspecie):
        self.__especie = novaEspecie

    @peso.setter
    def alteraPeso(self, novoPeso):
        self.__peso = novoPeso

    @alimentacao.setter
    def alteraAlimentacao(self, novaAlimentacao):
        self.__alimentacao = novaAlimentacao
