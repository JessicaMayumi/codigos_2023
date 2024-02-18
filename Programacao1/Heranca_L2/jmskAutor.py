from jmskPessoa import Pessoa
class Autor(Pessoa):
    def __init__(self, nome, dataNascimento, biografia):
        super().__init__(nome, dataNascimento)
        self.__biografia = biografia

    def __str__(self):
        return super().__str__() + "\nBiografia:" + self.__biografia

    @property
    def biografia(self):
        return self.__biografia