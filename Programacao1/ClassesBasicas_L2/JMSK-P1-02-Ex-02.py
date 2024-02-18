class MinhaLista:
    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.append(item)

    def apresentar(self):
        for i in self.itens:
            print(i, end=" ")

umaLista = MinhaLista()
umaLista.adicionar("a")
umaLista.adicionar(10)
umaLista.apresentar()