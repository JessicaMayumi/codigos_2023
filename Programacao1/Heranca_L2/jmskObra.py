from jmskParecer import Parecer
from jmskAutor import Autor
class Obra: 
    def __init__(self, titulo, ano):
        self.__titulo = titulo
        self.__ano = ano
        self.__listaPareceres = []
        self.__listaAutores = []

    def listaPareceres(self):
        pareceres = ""
        for parecer in self.__listaPareceres:
            pareceres += str(parecer) + "\n"
        return pareceres

    def listaPrimeiroParecer(self):
        return self.__listaPareceres[0]

    def listaUltimoParecer(self):
        return self.__listaPareceres[-1]

    def adicionaParecer(self, parecer): 
        self.__listaPareceres.append(parecer)

    def removerParecer(self, parecer):
        self.__listaPareceres.remove(parecer)

    def adicionaAutor(self, autor):
        self.__listaAutores.append(autor)
    
    def removeAutor(self, autor):
        self.__listaAutores.remove(autor)
    
    def listaAutores(self):
        autores = ""
        for autor in range(len(self.__listaAutores)):
            autores += str(self.__listaAutores[autor]) + "\n"
            return autores

    def __str__(self):
        return "Obra: " + str(self.__titulo) + "\nAno: " + str(self.__ano) + "\nAutores\n" + str(self.listaAutores()) + "\nPareceres\n" + str(self.listaPareceres())

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
