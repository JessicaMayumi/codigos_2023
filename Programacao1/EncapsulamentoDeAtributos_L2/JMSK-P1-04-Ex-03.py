class Aluno:
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
        
    def calculaMedia(self, nota1, nota2, nota3):
        notas = [nota1, nota2, nota3]
        soma = 0
        for nota in notas:
            soma += nota
            if nota < 0:
                nota = 0
            elif nota > 10:
                nota = 10
            else:
                nota = nota
        self.__nota1 = notas[0]
        self.__nota2 = notas[1]
        self.__nota3 = notas[2]

        return soma/3

    def aprovado(self):
        if aluno.calculaMedia(self.__nota1, self.__nota2, self.__nota3) >= 6:
            return True
        else:
            return False
        
    @property
    def notas(self):
        return self.__nota1 + self.__nota2 + self.__nota3
    
    def imprimir(self):
        return "Nome: " + str(self.__nome) + "\nCPF: " + str(self.__cpf) + "\nNota 1: " + str(self.__nota1) + "\nNota 2: " + str(self.__nota2) + "\nNota 3: " + str(self.__nota3) + "\nMédia: " + str(aluno.calculaMedia(self.__nota1, self.__nota2, self.__nota3)) + "\n"
    
aprovados = []
reprovados = []

def imprimirAprovados():
    strAprovados = ""
    for aluno in aprovados:
        strAprovados += str(aluno.imprimir()) + "\n"
    return strAprovados

def imprimirReprovados():
    strReprovados = ""
    for aluno in reprovados:
        strReprovados += str(aluno.imprimir()) + "\n"
    return strReprovados
    
soma = 0

while True: 
    pergunta = input("Deseja cadastrar um aluno? ( S ou N ):")
    if pergunta.upper() == "N":
        break
    if pergunta.upper() == "S":
        nome = input("Insira o nome do aluno: ")
        cpf = input("Insira o CPF do aluno: ")
        nota1 = float(input("Insira a primeira nota: "))
        nota2 = float(input("Insira a segunda nota: "))
        nota3 = float(input("Insira a terceira nota: "))
        aluno = Aluno(nome,cpf)
        mediaAluno = aluno.calculaMedia(nota1, nota2, nota3)
        if aluno.aprovado():
            aprovados.append(aluno)
        else:
            reprovados.append(aluno)
        soma += mediaAluno

media = soma/(len(aprovados)+len(reprovados))

print("Aprovados!\n" + imprimirAprovados())
print("Reprovados!\n" + imprimirReprovados())
print("A média geral da turma é ", media)