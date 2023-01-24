#Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
#Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
#przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
#wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi

from random import randint
from math import isqrt

def print_tab(tab):
    for line in tab:
        print(line)

def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(10,99)
    return T

def rowSums(A):
    n=len(A)
    tab=[0 for _ in range(n)]
    
    for row in range(n):
        currsum=0
        for col in range(n):
            currsum+=A[row][col]
        tab[row]=currsum

    return tab

def colSums(A):
    n=len(A)
    tab=[0 for _ in range(n)]
    
    for col in range(n):
        currsum=0
        for row in range(n):
            currsum+=A[row][col]
        tab[col]=currsum

    return tab
        

def twoTowers(T):
    N=len(T)
    rowSum=rowSums(T)
    colSum=colSums(T)
    maxSum=0
    x1,y1,x2,y2=0,0,0,0 #współrzędne wież z maxymalną sumą "szachowanych" pól

    for rowT1 in range(N):
        for colT1 in range(N):
            for rowT2 in range(N):
                for colT2 in range(N):
                    currSum=0
                    #przypadek gdy wieże są na tym samym polu
                    if(rowT1==rowT2 and colT1==colT2):
                        currSum=rowSum[rowT1]+colSum[colT1]-(2 * T[rowT1][colT1])
                    #przypadek gdy wieże są w tym samym rzędzie ale innej kolumnie
                    elif(rowT1==rowT2 and colT1!=colT2):
                        currSum=rowSum[rowT1]+colSum[colT1]+colSum[colT2]-(2 * T[rowT1][colT1])-(2 * T[rowT2][colT2])
                    #przypadek gdy wieże są w tej samej kolumnie ale innym rzędzie
                    elif(rowT1!=rowT2 and colT1==colT2):
                        currSum=rowSum[rowT1]+rowSum[colT2]+colSum[colT1]-(2 * T[rowT1][colT1])-(2 * T[rowT2][colT2])
                    #przypadek gdy wieże nie są w tej samej kolumnie ani w tym samym rzędzie
                    else:
                        currSum=rowSum[rowT1]+colSum[colT1]+colSum[colT2]
                        currSum-=(2 * T[rowT1][colT1])
                        currSum-=(2 * T[rowT2][colT2])
                        currSum-=T[rowT1][colT2]
                        currSum-=T[rowT2][colT1]

                    if(currSum>maxSum):
                        maxSum=currSum
                        x1,y1,x2,y2=rowT1,colT1,rowT2,colT2

    return (x1,y1,x2,y2)



def main():
    N=int(input("N: "))
    Tab=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(Tab,N)
    print_tab(Tab)
    print(twoTowers(Tab))

if __name__ == "__main__": main()