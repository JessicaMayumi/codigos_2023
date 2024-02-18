class Aluno:
    def __init__ (self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    def __str__(self) -> str:
        return "Nome: " + self.__nome + "\nMatrícula: " + str(self.__matricula) + "\n"
    
    def __eq__(self, outro_aluno) -> bool: #sobrecarga de operadores: criar meu próprio sinal de igual, exclusivo da classe Aluno
        if self.__nome == outro_aluno.__nome and self.__matricula == outro_aluno.__matricula:
            return True
        else:
            return False
        
    def __ne__(self, outro_aluno) -> bool:
        if self.__nome!=outro_aluno.__nome or self.__matricula!=outro_aluno.__matricula:
            return True
        else:
            return False
        
    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

