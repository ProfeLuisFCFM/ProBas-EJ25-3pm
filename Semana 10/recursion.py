def fibbo(num):
    lst = [0,1]
    if num == 1:
        return [0]
    elif num == 2:
        return [0, 1]
    else:
        for it in range(2,num+1):
            lst.append(lst[it-2]+lst[it-1])
    return lst


print(fibbo(9))

def factorial(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

def factorialRc(n):
    if n <=1:
        return 1
    else:
        return n*factorialRc(n-1)

import time

inicio1 = time.time()
print(factorial(79))
fin1 = time.time() - inicio1

inicio2 = time.time()
print(factorialRc(79))
fin2 = time.time() - inicio2 

print(fin1,fin2)