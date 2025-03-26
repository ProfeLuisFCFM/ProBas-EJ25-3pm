import time, math

def suma(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

def suma2(n):
    sum = 0
    for i in range(1,(n//2)+1):
        sum += i
        sum += (n+1)-i
    return sum

def suma4(n):
    sum = 0
    for i in range(1,(n//4)+1):
        sum += i
        sum += (n+1)-i
        sum += n//4 + i
        sum += (n-(n//4)+1)-i
    return sum

def cuantoTiempo(fn):
    inicio = time.time()
    fn(10)
    time.sleep(0.5)
    return (time.time() - inicio)*1e6



print(cuantoTiempo(suma))
print(cuantoTiempo(suma2))
print(cuantoTiempo(suma4))



