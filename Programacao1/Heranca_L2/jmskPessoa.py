class Pessoa:
    def __init__(self, nome, dataNascimento):
        self.__nome = nome
        self.__dataNascimento = dataNascimento
    
    def __str__(self):
        return "Nome: " + self.__nome + "\nData de Nascimento: " + self.__dataNascimento

    @property
    def nome(self):
        return self.__nome
    
    @property
    def dataNascimento(self):
        return self.__dataNascimento