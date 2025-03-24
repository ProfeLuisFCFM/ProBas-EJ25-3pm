
class Hola():
    def __init__(self,Nombre):
        self.Name = Nombre

    def getName(self):
        return self.Name



from abc import ABC, abstractmethod #Abstract Base Class

class Politopo2(ABC):
    def __init__(self,name='2-Politopo'):
        self.NombreFigura=name
        super().__init__()

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
    
    @staticmethod
    def getName(self):
        return self.NombreFigura
    

class Triangulo(Politopo2):
    def __init__(self,b = 1, h= 1, name='Tríangulo'):
        self.base = b
        self.haltura = h
        super().__init__(name)
    
    def area(self):
        return (self.base * self.haltura / 2)
    
    def perimetro(self):
        return (self.base * 3)
        

class Cuadrado(Politopo2):
    def __init__(self,l = 1, name='Cuadrado'):
        self.lado = l
        super().__init__(name)
    
    def area(self):
        return self.lado**2
    
    def perimetro(self):
        return self.lado * 4




if __name__ == '__main__':
    variahola = Hola("Luis")
    variable2 = Hola("Mario")
    print(variahola.getName())
    print(variable2.getName())
    tri = Triangulo(1,1,"Triangulo")
    print(tri.area())
    print(tri.perimetro())

import principal

