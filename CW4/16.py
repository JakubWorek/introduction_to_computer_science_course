#Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
#odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
#będących liczbami pierwszymi?

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
    if(num<2): return False
    if(num==2 or num==3): return True
    if(num%2==0 or num%3==0): return False

    i=5
    while(i<isqrt(num)+1):
        if(num%i==0): return False
        i+=2
        if(num%i==0): return False
        i+=4
    
    return True

def ex16(tab):
    cnt=0

    for row in tab:
        for elem in row:
            tmp=elem
            flag=True

            while(tmp>0):
                cyf=tmp%10
                if(not isPrime(cyf)):
                    flag=False
                    break
                tmp//=10
            
            if(flag):
                cnt+=1
                break
        if(cnt-1 != row): return False

    if(cnt==len(tab)): return True
    return False

def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)
    print(ex16(T))

if __name__ == "__main__": main()