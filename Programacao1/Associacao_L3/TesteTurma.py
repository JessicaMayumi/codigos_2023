from Aluno import Aluno
from Turma import Turma

listaTurma = []

while True:
    pergunta = input ("Deseja adicionar um aluno em alguma turma?( S ou N ): ")
    if pergunta.upper() == "N":
        break
    if pergunta.upper() == "S":
        # Verificar se a turma é igua ou diferente a uma que já exista
        perguntaTurmaCódigo = input("Em qual turma você deseja inserir o aluno? ( apenas o código da turma ): ")
        perguntaTurmaDescricao = input("Insira a descrição da turma: ")
        diferente = False #testar
        for turma in listaTurma:
            if turma.codigo == perguntaTurmaCódigo and turma.descricao == perguntaTurmaDescricao:
                diferente = True
                break
            else:
                diferente = False
        if diferente == False:
            turma = Turma(perguntaTurmaCódigo, perguntaTurmaDescricao)
            listaTurma.append(turma)

        # Verificar se já existe um aluno com a mesma matrícula na turma

        perguntaAlunoNome = input ("Insira o nome do aluno que você deseja adicionar: ")
        perguntaAlunoMatrícula = input ("Insira o número de matrícula do aluno que você deseja adicionar: ")
        aluno = Aluno(perguntaAlunoNome, perguntaAlunoMatrícula)

        listaTurma[listaTurma.index(turma)].addAluno(aluno)
        
for turma in listaTurma:
    print (turma)

# Para remover algum aluno
while True:
    pergunta2 = input("Deseja remover algum aluno? ( S ou N ): ")
    if pergunta2.upper() == "N":
        break
    if pergunta2.upper() == "S":
        # Remover a partir do nome
        perguntaRemoverNome = input("Deseja remover o aluno pelo nome? ( S ou N ): ")
        if perguntaRemoverNome.upper() == "S":
            perguntaNome = input("Insira o nome do aluno ( o mesmo do cadastro ) : ")
            for turma in listaTurma:
                    turma.removeAlunoNome(perguntaNome)
        # Remover a partir da Matrícula
        if perguntaRemoverNome.upper() == "N":
            perguntaRemoverMatricula = input("Deseja remover o aluno pela matrícula? ( S ou N ): ")
            if perguntaRemoverMatricula.upper() == "S":
                perguntaMatricula = input("Insira o número de matrícula do aluno: ")
                for turma in listaTurma:
                    turma.removeAlunoMatricula(perguntaMatricula)
                    
# Se a turma não houver nenhum aluno, ela sai da lista de Turmas
for turma in listaTurma:
    if len(turma.alunos) == 0:
        listaTurma.remove(turma)    

for turma in listaTurma:
    print (turma)

        
    