class Restaurante:
    def __init__(self, nome, endereco, telefone, cep, nota, id=None):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__cep = cep
        self.__nota = nota
        self.__id = id

    def estrelas(self):
        estrelinhas = [" ☆ ", " ☆ ", " ☆ "," ☆ "," ☆ ", " "]
        strEstrelinhas = ""
        for i in range(len(estrelinhas)):
            if i < int(self.__nota):
                estrelinhas[i] = " ★ "
        
        for i in estrelinhas:
            strEstrelinhas += i

        return strEstrelinhas

        '''
            strEstrelinhas += estrelinhas[i]
            if i < len(self.__nota):
                strEstrelinhas[i] = " ★ "
        return strEstrelinhas
        '''
        
    def __str__(self):
        return f"\033[1mNome:\033[0;0m\033[35m {self.__nome:<30}| \033[1mTelefone:\033[0;0m\033[35m {self.__telefone:<15}| \033[1mCEP:\033[0;0m\033[35m {self.__cep:<10}| \033[1mNota:\033[0;0m \033[33m{self.estrelas()}\033[0;0m\033[35m| \033[1mEndereço: \033[0;0m\033[35m{self.__endereco:<59}\033[0;0m" 
    
    # def formatarTelefone(self):
    # def formatarCEP(self):
    # def formatarNota(self):

    def imprimirLado(self):
        # print(f"{dado[0]:<30}{dado[1]:>3} anos")
        return f"\033[1m\033[36m| {self.__nome:<26}| {self.__telefone:<15}| {self.__cep:<10}| \033[33m{self.estrelas()}\033[1m\033[36m| {self.__endereco:<50}| {self.__id:<9}|\033[0;0m"

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novoNome):
        self.__nome = novoNome

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novoEndereco):
        self.__endereco = novoEndereco

    @property 
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novoTelefone):
        self.__telefone = novoTelefone

    @property
    def cep(self):
        return self.__cep
    
    @cep.setter
    def cep(self, novoCep):
        self.__cep = novoCep
    
    @property
    def nota(self):
        return self.__nota
    
    @nota.setter
    def nota(self, novaNota):
        self.__nota = novaNota

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, novoId):
        self.__id = novoId

#teste
