# definicao da classe (criacao da classe)
class Quadrado:
    def __init__ (self,lado):
        self.lado = lado
    
    def calcularArea(self):
        return self.lado * self.lado

    def calcularPerimetro(self):
        return self.lado * 4
    
    def imprimir(self):
        area = self.calcularArea()
        perimetro = self.calcularPerimetro()
        return "Lado: " + str(self.lado) +  " Área: " + str(area) + " Perímetro: " + str(perimetro) 
    
    def __str__(self):
        area = self.calcularArea()
        perimetro = self.calcularPerimetro()
        return "Lado: " + str(self.lado) +  " Área: " + str(area) + " Perímetro: " + str(perimetro) 
    


lista = []

# instanciacao de um objeto da classe quadrado 
q = Quadrado(7)    
lista.append(q)

q = Quadrado(5)
lista.append(q)

q  = Quadrado(3)
lista.append(q)


#for i in range(len(lista)):
#    print(lista[i].imprimir())

for objeto in lista:
    print(objeto)

for objeto in lista:
    print(objeto.imprimir())
