#Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy
#zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
#liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”

from math import isqrt
from random import randint

def isFib(a):
    if(a==0): return True
    if(a==1): return True

    f0=0; f1=1
    while (f0+f1<=a):
        next=f0+f1
        if(next==a): return True
        f0=f1
        f1=next

    return False

def isPrime(x):
    if(x==2 or x==3): return True
    if(x%2==0 or x%3==0 or x<=1): return False
    i=5
    while(i<isqrt(x)+1):
        if(x%i==0): return False
        i+=2
        if(x%i==0): return False
        i+=4
    return True

def wypelnij(T,N):
    for i in range(N):
        T[i]=randint(100,999)
    return T

def isWarunek(T,N):
    flag=False
    for i in range(N):
        if(isFib(i) and isPrime(T[i])): return False
        elif(not isFib(i) and isPrime(T[i])): flag=True

    if(flag): return True
    

def main():
    N=int(input("N: "))
    tab=[0 for _ in range(N)]
    wypelnij(tab,N)
    print(tab)
    print(isWarunek(tab,N))

if __name__ == "__main__": main()