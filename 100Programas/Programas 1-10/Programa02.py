#Problema 2: Calculadora simple que realice operaciones básicas
import os
#os.system('cls' if os.name == 'nt' else 'clear')

menu1 = """
#   Menú Principal
#
#   E -> Exponentes
#   M -> Multiplicaciones
#   D -> División
#   A -> Adición    
#   S -> Sustracción
#   X -> Salir
#
"""
bMenu1 = True

menu2 = """
#   Menú División
#
#   1 -> División
#   2 -> División Entera
#   3 -> División Residuo
#   4 -> Regresar a menú principal
#
"""
bMenu2 = True

def exponentes(base, potencia):
    return base ** potencia

def multiplicacion(factor1, factor2):
    return factor2 * factor1


def division(dividendo, divisor):
    bDiv0 = True
    if divisor != 0:
        return dividendo/divisor
    else:
        while bDiv0: 
           ndivisor = int(input("La división entre 0 es imposible todavía\n, ingrese otro valor para el divisor: "))
           if ndivisor != 0:
               bDiv0 = False
        return dividendo/ndivisor


def divisionEntera(dividendo, divisor):
    bDiv0 = True
    if divisor != 0:
        return dividendo//divisor
    else:
        while bDiv0: 
           ndivisor = int(input("La división entre 0 es imposible todavía\n, ingrese otro valor para el divisor: "))
           if ndivisor != 0:
               bDiv0 = False
        return dividendo//ndivisor    
    
def divisionResiduo(dividendo, divisor):
    bDiv0 = True
    if divisor != 0:
        return dividendo%divisor
    else:
        while bDiv0: 
           ndivisor = int(input("La división entre 0 es imposible todavía\n, ingrese otro valor para el divisor: "))
           if ndivisor != 0:
               bDiv0 = False
        return dividendo%ndivisor      

def leerNumeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    return num1, num2 


def divisionMenu(bMenu2):
    bandera = bMenu2
    while bandera:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(menu2)
        op2 = int(input("Ingrese la opción deseada: "))
        if op2 == 1:
            t1 = leerNumeros()
            print(division(t1[0],t1[1]))
            tskip = input("\n\nPresione tecla para continuar..")
        elif op2 == 2:
            t2 = leerNumeros()
            print(divisionEntera(t2[0],t2[1]))
            tskip = input("\n\nPresione tecla para continuar..")
        elif op2 == 3:
            t3 = leerNumeros()
            print(divisionResiduo(t3[0],t3[1]))           
            tskip = input("\n\nPresione tecla para continuar..")
        elif op2 == 4:
            bMenu2 = False
            break            
        else:
            print("Opción inválida.")
    
        
def adicion(num1, num2):
    return num1 + num2

def sustraccion(num1, num2):
    return num1 - num2


while bMenu1:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(menu1)
    op = input("Ingrese la opción deseada: ")
    op = op.upper()
    if op == 'E':
        tE = leerNumeros()
        print(exponentes(tE[0],tE[1]))
        tskip = input("\n\nPresione tecla para continuar..")
    elif op == 'M':
        tM = leerNumeros()
        print(multiplicacion(tM[0],tM[1]))
        tskip = input("\n\nPresione tecla para continuar..")
    elif op == 'D':
        divisionMenu(bMenu2)
    elif op == 'A':
        tA = leerNumeros()
        print(adicion(tA[0],tA[1]))
        tskip = input("\n\nPresione tecla para continuar..")
    elif op == 'S':
        tS = leerNumeros()
        print(sustraccion(tS[0],tS[1]))
        tskip = input("\n\nPresione tecla para continuar..")
    elif  op == 'X':
        bMenu1 = False
    else:
        print("Opción inválida")
        

