#Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną 
# i zwraca sumę iloczynów elementów wszystkich niepustych podzbiorów 
# zbioru podzielników pierwszych tej liczby. Można założyć,
#że liczba podzielników pierwszych nie przekracza 20, zatem 
# w pierwszym etapie funkcja powinna wpisać podzielniki do tablicy pomocniczej.
#  Przykład: 60 → [2, 3, 5] → 2 + 3 + 5 + 2 ∗ 3 + 2 ∗ 5 + 3 ∗ 5 + 2 ∗ 3 ∗ 5 = 71

s=0
                                #obecny iloczyn
def SumOfIl(div: list[int], i:int, il:int):
    if(div[i]==-1):
        if(il==1): return

        global s
        s+=il
        return

    SumOfIl(div,i+1,il)
    SumOfIl(div,i+1,il*div[i])


def Dividers(num:int):
    i=2
    j=0
    divs=[-1]*20
    while(num>1):
        if(num%i==0):
            divs[j]=i
            j+=1
            while(num%i==0):
                num//=i
        i+=1

    return divs

n=60
SumOfIl(Dividers(n),0,1)
print(s)
