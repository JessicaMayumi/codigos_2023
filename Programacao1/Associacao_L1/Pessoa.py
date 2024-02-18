from Endereco import Endereco
class Pessoa:
    def __init__ (self, nome, idade, endereco):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco

    def __str__(self) -> str:
        return "Nome: " + self.__nome + "\nIdade: " + str(self.__idade) + "\nEndereço: \n" + str(self.__endereco)

    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
