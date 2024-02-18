class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "Ponto x: " + str(self.__x) + "\t|\tPonto y: " + str(self.__y)
    
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
class Poligono:
    def __init__(self):
        self.__pontos = []

    def addPonto(self, pontos):
        self.__pontos.append(pontos)

    def area(self):
        if len(self.__pontos) < 3:
            return "Polígono inválido, insira pelo menos 3 pontos."
        area = 0
        for i in range(len(self.__pontos)):
            if i == (len(self.__pontos)-1):
                area += (self.__pontos[i].x * self.__pontos[0].y) - (self.__pontos[0].x * self.__pontos[i].y)
            else:
                area += (self.__pontos[i].x * self.__pontos[i+1].y) - (self.__pontos[i+1].x * self.__pontos[i].y)
        return area/2
    
    def perimetro(self):
        if len(self.pontos) < 3:
            return "Polígono inválido, insira pelo menos 3 pontos."
        perimetro = 0
        for i in range(len(self.__pontos)):
            if i == (len(self.__pontos)-1):
                perimetro += ((self.__pontos[0].x - self.__pontos[i].x)**2+(self.__pontos[0].y-self.__pontos[i].y)**2)**0.5
            else:
                perimetro += ((self.__pontos[i+1].x - self.__pontos[i].x)**2+(self.__pontos[i+1].y-self.__pontos[i].y)**2)**0.5
        return perimetro

    def __str__(self):
        strPontos = ""
        for ponto in self.__pontos:
            strPontos += "\nParcela " + str(self.__pontos.index(ponto)+1) + ": " + str(ponto)
        return "\t--- Pontos--- \n" + strPontos + "\nÁrea: " + str(self.area()) + "\nPerímetro: " + str(self.perimetro())
    
    @property
    def pontos(self):
        return self.__pontos
    
x = int(input("Insira um valora para o ponto x: "))
y = int(input("Insira um valora para o ponto y: "))
pontos = Ponto(x,y)
p = Poligono()
p.addPonto(pontos)

while True:
    x = (input("Insira outro valor para x (enter para parar): "))
    if x == "":
        break
    y = int(input("Insira outro valora para y: "))
    pontos = Ponto(int(x),y)
    p.addPonto(pontos)

print(p)



