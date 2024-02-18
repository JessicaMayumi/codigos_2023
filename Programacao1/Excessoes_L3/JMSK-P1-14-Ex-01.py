import abc

class Animal(abc.ABC):
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @abc.abstractmethod
    def fazer_barulho(self):
        pass

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def fazer_barulho(self):
        return "Au Au!"

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)  

    def fazer_barulho(self):
        return "Meow! "  

class Vaca(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)    

    def fazer_barulho(self):
        return "Muuuuuuh! "

try:    
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    print("Tipo:\n1- Cachorro\n2- Gato\n3- Vaca")
    tipo = int(input("Tipo: "))

    if tipo == 1:
        animal = Cachorro(nome, idade)

    elif tipo == 2:
        animal = Gato(nome, idade)

    elif tipo == 3:
        animal = Vaca(nome, idade)

    else: 
        raise ValueError("Animal Desconhecido, digite um número válido! ")

    print(animal.fazer_barulho())

#except:
#    print("Ocorreu um erro!")

except ValueError as e:
    print("Erro:", e)
