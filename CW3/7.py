# program wypełniający N-elementową tablicę t liczbami pseudolosowymi z zakresu
#1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste

from random import randint

def wypelnij(T,N):
    for i in range(N):
        T[i]=randint(1,1000)
    return T

def checknieparz(num):
    cyf=0
    while(num >0):
        cyf=num%10
        if(cyf%2==0): return False
        num//=10
    return True

def checktab(T,N):
    for i in range(N):
        if(checknieparz(T[i])==True): return True
    return False

def main():
    N=int(input("N: "))
    tab=[0 for _ in range(N)]
    wypelnij(tab,N)
    print(tab)
    print(checktab(tab,N))

if __name__ == "__main__": main()