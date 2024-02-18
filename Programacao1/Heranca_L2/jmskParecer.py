from jmskParecista import Parecista
class Parecer:
    def __init__(self, parecista, data, conteudo):
        self.__parecista = parecista
        self.__data = data
        self.__conteudo = conteudo

    def __str__(self):
        return str(self.parecista) + "\nData: " + str(self.__data) + "\nConteúdo: " + self.__conteudo

    @property
    def parecista(self):
        return self.__parecista
    
    @property 
    def data(self):
        return self.__data
    
    @property
    def conteudo(self):
        return self.__conteudo