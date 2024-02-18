from datetime import datetime 
from RestauranteDAO import *

def dataFormatada(data_em_txt): #quando vem do input
    try: 
        if not isinstance(data_em_txt, str):
          data_em_txt = str(data_em_txt)

        if "-" in data_em_txt:
            data_em_txt = data_em_txt.replace("-", "/")
        data = datetime.strptime(data_em_txt, '%Y/%m/%d').date()
        return data.strftime('%d/%m/%Y')
    except  (ValueError, TypeError):
        print("\033[31mData inválida!\033[m")

def dataSQL(data_ptbr): # para entrar no banco de dados
    data_ptbr = data_ptbr.replace("/", "-")
    data_obj = datetime.strptime(data_ptbr, '%d-%m-%Y')
    return data_obj.strftime('%Y-%m-%d')

#data_atual = datetime.today()
#data_txt = '{}/{};{}' .format(data_atual.day, data_atual.month, data_atual.year)

class Funcionario():
    def __init__(self, nome, cargo, salario, cpf, dataContratacao, restauranteID, funcionarioID = None):
        self.__funcionarioID = funcionarioID
        self.__cpf = cpf
        self.__nome = nome
        self.__cargo = cargo
        self.__salario = salario
        self.__dataContratacao = dataContratacao
        self.__restauranteID = restauranteID

        # def idade(self):
        #     diff = data_atual - self.__dataNascimento
        #     days = diff.days
        #     years, days = days // 365, days % 365
        #     months, days = days // 30, days % 30

        #     seconds = diff.seconds
        #     hours, seconds = seconds // 3600, seconds % 3600
        #     minutes, seconds = seconds // 60, seconds % 60

        #     return "Desde {} se passaram {} anos, {} meses, {} dias, {} horas, {} minutos e {} segundos.".format(dataFormatada(self.__dataNascimento), years, months, days, hours, minutes, seconds)
   
    @property
    def restauranteID(self):
        return self.__restauranteID
 
    @restauranteID.setter
    def restauranteID(self, restauranteID):
        self.__restauranteID = restauranteID
 
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf
 
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo
 
    @property
    def salario(self):
        return self.__salario
 
    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    @property 
    def dataContratacao(self):
        return self.__dataContratacao

    @dataContratacao.setter
    def dataContratacao(self, dataContratacao):
        self.__dataContratacao = dataContratacao    

    @property
    def funcionarioID(self):
        return self.__funcionarioID
    
    @funcionarioID.setter
    def funcionarioID(self,funcionarioID):
        self.funcionarioID = funcionarioID

    def __str__(self):
        return f"Cpf: {self.__cpf}\nNome: {self.__nome}\nCargo: {self.__cargo}\nSalário: {self.__salario}\nData de Contratação: {str(dataFormatada(self.__dataContratacao))}\nID do Restaurante: {self.__restauranteID}"
    
    def imprimirLado(self):
        restaurante = RestauranteDAO().buscaRestaurante(self.__restauranteID)
        # print(f"{dado[0]:<30}{dado[1]:>3} anos")
        return f"\033[1m\033[36m| {self.__nome:<32}| {self.__cargo:<16}| {str(self.__salario):<11}| \033[33m\033[1m{str(self.__cpf):<16}\033[1m\033[36m| {dataFormatada(self.__dataContratacao):<14}| \033[36m{restaurante.nome:<36} |\033[0;0m"

# converter data pt-BR para SQL
# data = datetime.strptime('26/08/2018', '%d/%m/%Y').date()
# print(data)
# funcionario = Funcionario("a", "b", 12.23, 123, "2006-06-06", 1)
# funcionario = Funcionario("a", "b", 12.23, 123, "10/10/1991", 1)
# print(funcionario)
