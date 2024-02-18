import abc

class Funcionario(abc.ABC):
    def __init__(self, nome, cpf, salario):
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario

    def getBonificacao(self):
        self.__salario += (self.__salario*0.1)

    def __str__(self):
        return "Nome: " + self.__nome + "\nCPF: " + self.__cpf + "\nSalário: " + str(self.__salario)

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    def salario(self):
        return self.__salario
    
class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, senha, qtde):
        super().__init__(nome, cpf, salario)
        self.__senha = senha 
        self.__qtde = qtde

    def getBonificacao(self):
        return super().getBonificacao() + (super.getBonificacao() * 0.15)
    
    def __str__(self):
        return super().__str__() + "\nSenha: " + str(self.__senha) + "\nQuantidade de Gerenciados: " + str(self.__qtde)
    


#--------------------------------------------------------------------------------


class ControleDeBonificacoes:
    def __init__(self):
        self.__totalBonificacao = 0
        self.__listaFuncionarios = []
    
    @property
    def listaFuncionarios(self):
        return self.__listaFuncionarios
    
    @property
    def totalBonificacao(self):
        return self.__totalBonificacao


    def registra(self, funcionario):
        self.__listaFuncionarios.append(funcionario)

    def getTotalBonicicacoes(self):
        for funcionario in self.__listaFuncionarios:
            print("oiiiii"+funcionario)
            self.__totalBonificacao += (funcionario.salario *0.1)

    def __str__(self):
        f = ""
        for funcionario in self.__listaFuncionarios:
            f += "\n" + str(funcionario)
        return "Total de bonificações: " + str(self.__totalBonificacao) + "\n" + f
   
    @property
    def totalBonificacao(self):
        return self.__totalBonificacao 


gerente = Gerente("Jessica","123456",1500,"123",5)
print(gerente)

f1 = Funcionario("Livia", "234567", 1600)
f2 = Funcionario("Carol", "345678", 1650)
print(f1)
print(f2)

c = ControleDeBonificacoes()
c.registra(f1)
c.registra(f2)
print(len(c.listaFuncionarios))
print(str(c.totalBonificacao()))

