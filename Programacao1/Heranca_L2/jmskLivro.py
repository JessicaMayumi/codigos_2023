from jmskObra import Obra
from jmskAutor import Autor
from jmskParecer import Parecer
class Livro(Obra):
    def __init__(self, titulo, ano, genero, editor, qtdPaginas):
        super().__init__(titulo, ano)
        self.__genero = genero
        self.__editor = editor
        self.__qtdPaginas = qtdPaginas

    def __str__(self):
        return super().__str__()

    @property
    def genero(self):
        return self.__genero
    
    @property
    def editor(self):
        return self.__editor
    
    @property
    def qtdPaginas(self):
        return self.__qtdPaginas