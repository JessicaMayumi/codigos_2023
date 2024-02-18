#'''
class Cliente:
    def __init__(self, nome):
        if(tem_numeros(nome)):
            print("tem número")
        else:
            self.nome = nome
            
    def __str__(self):
        try:
            return "Nome: " + self.nome
        except:
            return "Erro"

#verificador de números em uma string
def tem_numeros(string):
    return any(char.isdigit() for char in string)
    
    #@property
    #def nome(self):
    #    return self.__nome
#'''
try:
    '''
    a = int(input("numerador: "))
    b = int(input("denominador: "))
    r = a/b
    '''
    c = Cliente("rudney")
    
#except:
#    print("Problema!")

#Apresenta o erro já dado pelo VScode
except Exception as erro:
    print("O proble encontrado foi {}" .format(erro.__class__))

#except ZeroDivisionError: #(Tipo de erro)
#    print("Não foi possível dividir um número por Zero!")

else:
    #print("O resultado é {:.2f}" .format(r))
    
    print(c)

finally:
    print("não Volte !")