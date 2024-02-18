from Cliente import Cliente

class ContaCorrente:
    def __init__(self, numero, saldoInicial, cliente):
        self.__numero = numero
        self.__saldoInicial = saldoInicial
        self.__cliente = cliente

    def __str__(self) -> str:
        return "- Cliente\n" + str(self.__cliente) + "\nNúmero: " + str(self.__numero) + "\nSaldo Inicial: " + str(self.__saldoInicial)
    

    @property
    def numero(self):
        return self.__numero

    @property
    def saldoInicial(self):
        return self.__saldoInicial
