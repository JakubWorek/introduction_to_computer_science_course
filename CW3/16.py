#Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą wartość typu bool oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
#jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
#wartości)

from random import randint

def wypelnij(T,N):
    for i in range(N):
        T[i]=randint(100,999)
    return T

def isWarunek(T,N):
    mini=T[0]
    maxi=T[0]

    for i in range(1,N):
        if(T[i]<mini): mini=T[i]
        elif(T[i]>maxi): maxi=T[i]

    flagmin=False
    flagmax=False
    for i in range(0,N):
        if(T[i]==mini and flagmin==True): return False
        if(T[i]==mini and flagmin==False): flagmin=True
        if(T[i]==maxi and flagmax==True): return False
        if(T[i]==maxi and flagmax==False): flagmax=True

    if(flagmin and flagmax): return True


def main():
    N=int(input("N: "))
    tab=[0 for _ in range(N)]
    wypelnij(tab,N)
    print(tab)
    print(isWarunek(tab,N))

if __name__ == "__main__": main()