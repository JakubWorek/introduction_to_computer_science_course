#Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
#będącą liczbą pierwszą?

from random import randint
from math import isqrt

def print_tab(tab):
    for line in tab:
        print(line)

def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(100,999)
    return T

def isPrime(num):
    if(num==2 or num==3): return True
    if(num%2==0 or num%3==0): return False

    i=5
    while(i<isqrt(num)+1):
        if(num%i==0): return False
        i+=2
        if(num%i==0): return False
        i+=4
    
    return True

def ex15(tab):
    for row in tab:
        cnt=0
        for elem in row:
            tmp=elem
            while(tmp>0):
                cyf=tmp%10
                if(isPrime(cyf)):
                    cnt+=1
                    break
                tmp//=10
        if(cnt==len(tab)): return True
    return False

def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)
    print(ex15(T))

if __name__ == "__main__": main()