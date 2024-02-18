import math
class Cilindro:
    def __init__(self, raio, altura):
        self.__raio = raio
        self.__altura = altura

    def calculaVolume(self):
        return math.pi * (self.__raio * self.__raio) * self.__altura     

    def calculaAreaBase(self):
        return (2 * math.pi) * self.__raio * (self.__raio + self.__altura)

    def calculaAreaLateral(self):
        return (2 * math.pi) * self.__raio * self.__altura

    def calculaAreaTotal(self):
        return (self.calculaAreaBase() * 2) + self.calculaAreaLateral()
    
raio = [2,2,3,10,7]
altura = [2,4,10,8,12]

print("Raio\t\tAltura\t\tVolume\t\tBase\t\tLateral\t\tTotal")
for i in range(len(raio)):
    c = Cilindro(raio[i], altura[i])
    print ("{}\t\t{}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}\t\t{:.2f}" .format(raio[i], altura[i], c.calculaVolume(), c.calculaAreaBase(), c.calculaAreaLateral(), c.calculaAreaTotal()))
