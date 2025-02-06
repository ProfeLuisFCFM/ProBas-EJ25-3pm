conjunto = set()
lista = list()
tupla = tuple()
diccionario = dict()

entero = 0
flotante = 0.0
string = ""

print(bool(entero),bool(flotante),bool(string))
print(bool(conjunto),bool(lista),bool(tupla),bool(diccionario))

rango = range(0)
enumerador = enumerate([])

print(bool(rango), bool(enumerador))



op = True
suma = 0
while True and op:
    valor = int(input("Agregue un numero: "))
    suma += valor
    op = bool(input("ingrese un número para continuar: "))
    if op:
        continue
    else:
        print(suma)
        break
    
