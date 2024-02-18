from jmskPessoa import Pessoa
class Parecista(Pessoa):
    def __init__(self, nome, dataNascimento,honorario):
        super().__init__(nome, dataNascimento)
        self.__honorario = honorario
    
    def __str__(self):
        return str(super().__str__()) + "\nHonorário:" + self.__honorario

    @property
    def honorario(self):
        return self.__honorario