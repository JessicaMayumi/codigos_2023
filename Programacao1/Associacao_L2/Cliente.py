class Cliente:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    
    def __str__(self) -> str:
        return "Nome: " + self.__nome + "\nCPF: " + self.__cpf
        

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf
