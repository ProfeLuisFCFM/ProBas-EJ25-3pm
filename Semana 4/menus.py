Pep8 =f"""                                     ___,,___
                                ,d8888888888b,_
                            _,d889'        8888b,
                        _,d8888'          8888888b,
                    _,d8889'           888888888888b,_
                _,d8889'             888888889'688888, /b
            _,d8889'               88888889'     `6888d 6,_
         ,d88886'              _d888889'           ,8d  b888b,  d\
       ,d889'888,             d8889'               8d   9888888Y  )
     ,d889'   `88,          ,d88'                 d8    `,88aa88 9
    d889'      `88,        ,88'                   `8b     )88a88'
   d88'         `88       ,88                   88 `8b,_ d888888
  d89            88,      88                  d888b  `88`_  8888
  88             88b      88                 d888888 8: (6`) 88')
  88             8888b,   88                d888aaa8888, `   'Y'
  88b          ,888888888888                 `d88aa `88888b ,d8
  `88b       ,88886 `88888888                 d88a  d8a88` `8/
   `q8b    ,88'`888  `888'"`88          d8b  d8888,` 88/ 9)_6
     88  ,88"   `88  88p    `88        d88888888888bd8( Z~/
     88b 8p      88 68'      `88      88888888' `688889`
     `88 8        `8 8,       `88    888 `8888,   `qp'
       8 8,        `q 8b       `88  88"    `888b
       q8 8b        "888        `8888'
        "888                     `q88b
                                  "888'
"""



menuPrincipal = f"""
\r \v
#####################################################################
##                                                                 ##
##              1.- Print hola Mundo                               ##
##              2.- Suma 2 numeros                                 ##
##              3.- Cerrar                                         ## 
##                                                                 ##
#####################################################################
"""


BanderaMenuPrincipal = True

while BanderaMenuPrincipal:
    print(menuPrincipal)
    oPrincipal = input("Introduzca una opción: ")
    if oPrincipal == '1':
        print("hola mundo")
    elif oPrincipal == '2':
        num1 = int(input("Ingresa a:"))
        num2 = int(input("Ingresa b:"))
        print("La suma es: ",num1+ num2)
    else:
        BanderaMenuPrincipal = False

      


