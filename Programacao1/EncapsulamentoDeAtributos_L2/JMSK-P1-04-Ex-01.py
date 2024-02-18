class Paralelepipedo:
    def __init__(self, altura, largura, profundidade):
        self.__altura = altura
        self.__largura = largura
        self.__profundidade = profundidade

    def calculaArea(self):
        return 2 * (self.__largura * self.__profundidade + self.__largura * self.__altura + self.__profundidade * self.__altura)

    def calculaVolume(self):
        return self.__altura * self.__largura * self.__profundidade

altura = [2,4,10,8,20]
largura = [2,2,3,10,30]
profundidade = [2,6,7,5,50]

print ("Altura\tLargura\tProfundidade\tÁrea\tPerímetro")
for i in range(len(altura)):
    p = Paralelepipedo(altura[i], largura[i], profundidade[i])
    print ("{}\t{}\t{}\t\t{}\t{}" .format(altura[i], largura[i], profundidade[i], p.calculaArea(), p.calculaVolume()))

