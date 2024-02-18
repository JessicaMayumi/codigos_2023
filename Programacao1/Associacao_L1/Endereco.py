class Endereco: 
    def __init__ (self, rua, numero, bairro, cidade, cep):
        self.__rua = rua
        self.__numero = numero
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep

    def __str__(self) -> str:
        return "Rua: " + self.__rua + "\nNúmero: " + str(self.__numero) + "\nBairro: " + self.__bairro + "\nCidade: " + self.__cidade + "\nCep: " + self.__cep
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def cep(self):
        return self.__cep
