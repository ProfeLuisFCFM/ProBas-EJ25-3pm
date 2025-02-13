#problema 10:

path = "C:/Users/Aula 105/Desktop/"
name = "miarchivo"
ext = "lagr"


with open(path+name+"."+ext,"r", encoding="utf8") as miarchivo:
    #for i in range(10):
    #    print(i, file=miarchivo)
    for line in miarchivo.readlines():
        line = line.replace("\n", "")
        print(line)

    lista = [90, 95, 88]

    print("1er P", "2do P", "3er P", "Prom", sep="\t")
    print(lista[0], lista[1], lista[2], sum(lista)/len(lista), sep="\t")



archivito = open(path+name+"1.txt","w", encoding="utf8")

print("Mi archivio está corrioso.",file =archivito)


archivito.close()