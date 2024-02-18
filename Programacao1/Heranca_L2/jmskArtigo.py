from jmskObra import Obra
from jmskAutor import Autor
from jmskParecer import Parecer
class Artigo(Obra):
    def __init__(self, titulo, ano, revista, anoPublicacao):
        super().__init__(titulo, ano)
        self.__revista = revista
        self.__anoPublicacao = anoPublicacao

    def __str__(self):
        return str(super().__str__()) + "\nRevista: " + self.__revista + "\nAno de Publicação: " + str(self.__anoPublicacao)

    @property 
    def revista(self):
        return self.__revista
    
    @property 
    def anoPublicacao(self):
        return self.__anoPublicacao
