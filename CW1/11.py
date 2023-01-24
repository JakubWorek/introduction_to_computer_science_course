# program wyszukujący liczby zaprzyjaźnione mniejsze od miliona

def sumaDzielnikow(a):
    suma=0
    for i in range(1,int(a**0.5)+1):
        if(a%i==0):
            suma+=i
            if(a/i != i):
                suma+=int(a/i)
    return suma-a

for i in range(1, 1000000):
    sumOfFactors=sumaDzielnikow(i)
    if(i>sumOfFactors and i == sumaDzielnikow(sumOfFactors)):
        print(sumOfFactors, "i", i)