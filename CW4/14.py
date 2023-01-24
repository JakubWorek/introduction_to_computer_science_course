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
    

def convertTab(T):
    N=len(T)
    ones=[[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            num=T[row][col]
            cntOne=0
            while(num > 0):
                if(num%2==1): cntOne+=1
                num//=2
            ones[row][col]=cntOne
    return ones


def cntEqOnes(T1,T2):
    onesT1=convertTab(T1)
    onesT2=convertTab(T2)
    leng1=len(T1)
    leng2=len(T2)

    print_tab(T2)
    print("-----")
    print_tab(onesT2)
    print("-----")
    print_tab(T1)
    print("-----")
    print_tab(onesT1)
    print("-----")

    for rowT1 in range(leng2-leng1+1):
        for colT1 in range(leng2-leng1+1):
            cnt=0
            for rowT2 in range(leng2):
                for colT2 in range(leng2):
                    if(onesT1[rowT1][colT1]==onesT2[rowT2][colT2]): cnt+=1
            if((cnt/(leng2*leng2))>(1/3)): return True
    
    return False
            

def main():
    N2=int(input("N: "))
    N1=randint(1,N2)
    T1=[[0 for _ in range(N1)] for _ in range(N1)]
    wypelnij(T1,N1)
    T2=[[0 for _ in range(N2)] for _ in range(N2)]
    wypelnij(T2,N2)
    print(cntEqOnes(T1,T2))

if __name__ == "__main__": main()