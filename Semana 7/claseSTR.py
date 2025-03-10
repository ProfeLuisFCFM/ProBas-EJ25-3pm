'''
#Tipo Básico
bool()
int()
float()
#Tipo básico que se comporta como estructurado
str()
#Tipo Estructurado
list()
tuple()
set()
#Tipo estructurado más complejo
dict()
'''
entero = 1234
flotante = 3.1416

string = 'Senbonzakura Kageyoshi'

#for letra in string:
#    print(letra)

#GUI = Graphic User Interface (Ventanas en Windows)
#CLI = Command Line Interface (CMD)


str2 = string.capitalize()

print(string, str2)



print(string.count('a'))

string.encode('utf-8')

OP = "TVアニメ『#ONEPIECE』 全話ライブ配信プロジェクト 「ANYTIME ONE PIECE」 ▼YouTube ライブ配信中 本日3/10～11までの 配信エピソードを紹介！ #いつでもワンピース ▼詳細はこちら"

print(string.lower().count('s'))

print(string.upper()) 

print(string.endswith('shi'))

print(string.startswith('Sen'))


print(string.find('akura'))


import math

print("{:.100}".format(math.pi))

print(f"{string}")

print(string.join('|||'))