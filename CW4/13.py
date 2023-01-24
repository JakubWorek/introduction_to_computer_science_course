#Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą. Dana jest tablica
#T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która zeruje elementy nie posiadające
#liczby komplementarnej

from random import randint
from math import isqrt

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(11,99)
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


def hasComplementary(T,N):
    
    for row in range(N):
        for col in range(N):
            flag=False
            for i in range(N):
                for j in range(N):
                    if(T[i][j]==0 or (row==i and col==j)): continue
                    currNum=T[row][col]+T[i][j]
                    if(isPrime(currNum)): flag=True; break

            if(not flag): T[row][col]=0
    print_tab(T)

    
def main():
    N=int(input("N: "))
    T1=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T1,N)
    print_tab(T1)
    print("----------")
    hasComplementary(T1,N)

if __name__ == "__main__": main()