class Circulo:
    def __init__ (self,raio):
        self.raio = raio

    def calcularArea(self):
        return (self.raio * self.raio) * 3.14
    
    def calcularPerimetro(self):
        return 2 * 3.14 * self.raio
    
    def imprimir(self):
        area = self.calcularArea()
        perimetro = self.calcularPerimetro()
        return "raio: " + str(self.raio) +  " Área: " + str(area) + " Perímetro: " + str(perimetro) 
    

c = Circulo(2)
print(c.imprimir())