from Aluno import Aluno

class Turma:
    def __init__(self, codigo, descricao):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__alunos = []

    def addAluno(self, aluno):
        for aluno_da_lista in self.__alunos:
            if aluno_da_lista == aluno:
                return
        self.__alunos.append(aluno)
            

    def removeAlunoMatricula(self, matricula):
        for aluno in self.__alunos:
            if str(aluno.matricula) == str(matricula):
                self.__alunos.remove(aluno)

    def removeAlunoNome(self, nome):
        for aluno in self.__alunos:
            if aluno.nome.upper() == nome.upper():
                self.__alunos.remove (aluno)

    def __str__(self):
        turma = ""
        for aluno in self.__alunos:
            #print(aluno)
            turma += str(aluno) + "\n"
        return "\nCódigo da Turma: " + str(self.__codigo) + "\nDescrição da turma: " + str(self.__descricao) + "\n\nAlunos:\n" + turma
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def alunos(self):
        return self.__alunos
'''
a1 = Aluno("Jessica", "23456")
a2 = Aluno("Livia", "12345")
print(a1==a2)
print(a1!=a2)
#print(a1)
#print(a2)
t1 = Turma("123", "201")
t1.addAluno(a1)
t1.addAluno(a2)

a3 = Aluno("Jessica", "23456")
t1.addAluno(a3)
print(t1)

t2 = Turma("INF-201", "EMI INformatia 2o ano")

print(t2)

t1.removeAlunoNome("Jessica")
print(t1)

'''