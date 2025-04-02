#Elegante

dic1 = {1484412: "Luis Angel Gutierrez", }

fichero = open("Holamundo.txt","w")

fichero.write(str(dic1))

fichero.close()

#Rápida

path = "C:\\Users\\Aula 105\\Documents\\Github\\ProBas-EJ25-3pm\\Semana 10\\"
nombre = "divideyvenceras.py"

with open(path+nombre,"r", encoding="utf8") as fichero2:
    for line in fichero2.readlines():
        print(line)


#Uso en PIA:

sqr = lambda x: x**2
sqrt = lambda x: x**0.5
print(sqr(5),sqrt(169))

with open("funciones.pia","w") as pia:
    pia.write("lambda x: x**2")
    pia.write("lambda x: x**0.5")
