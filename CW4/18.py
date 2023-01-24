#Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
#wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
#podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
#maksymalnego podciągu

from random import randint
from math import isqrt

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,9)
    return T


def ex18(T):
    N=len(T)
    result=0
    for row in range(N):
        for col in range(N):
            for i in range(1,11):
                if(row+i<N):
                    suma=0
                    for x in range(row,row+i+1):
                        suma+=T[x][col]
                    result=max(result,suma)
                if(col+i<N):
                    suma=0
                    for x in range(col,col+i+1):
                        suma+=T[row][x]
                    result=max(result,suma)
    return result


def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)
    print(ex18(T))

if __name__ == "__main__": main()