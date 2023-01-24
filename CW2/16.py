#Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
#w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5∗17, 8+5 = 5+1+7. Napisać program wypisujący
#liczby Smitha mniejsze od 1000000

def rozklad(n):
    cz=2 #potencjalny czynnik
    my_list=[] #lista czynników

    while(n>1):
        while(n%cz==0): 
            my_list.append(cz)
            n=n/cz
        cz+=1

    return my_list

def suma(liczba):
    suma=0 # zmienna na sume cyfr
    while(liczba>0):
        k=liczba%10
        suma +=k
        liczba=int(liczba/10)
    return suma

def smitha(n):
    for i in range(1, n):
        lista=rozklad(i)
        if(len(lista)>1):
            sumal=suma(i)
            sumap=0
            for j in lista:
                sumap+=suma(j)

            if(sumap==sumal): print(i)

def testsmith(n):
    lista=rozklad(n)
    sumal=suma(n)
    print(sumal)
    sumap=0
    for j in lista:
        print(j)
        sumap+=suma(j)

    if(sumap==sumal): print("Tak")


def main():
    smitha(1000000)
    #testsmith(202)
    
if __name__ == "__main__": main()