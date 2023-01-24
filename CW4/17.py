#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję która
#zwraca wiersz i kolumnę dowolnego elementu, dla którego suma otaczających go elementów jest największa

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

def maxNeiSum(T):
    N=len(T)
    maxSum=0
    currSum=0
    maxRow=0
    maxCol=0

    #LG rog
    currSum+=T[0][1]
    currSum+=T[1][0]
    currSum+=T[1][1]
    if(currSum>maxSum):
        maxSum=currSum
        maxRow=0
        maxCol=0
    currSum=0
    
    #PG rog
    currSum+=T[0][N-2]
    currSum+=T[1][N-2]
    currSum+=T[1][N-1]
    if(currSum>maxSum):
        maxSum=currSum
        maxRow=0
        maxCol=N-1
    currSum=0
    
    #LD rog
    currSum+=T[N-2][0]
    currSum+=T[N-2][1]
    currSum+=T[N-1][1]
    if(currSum>maxSum):
        maxSum=currSum
        maxRow=N-1
        maxCol=0
    currSum=0

    #PD rog
    currSum+=T[N-2][N-2]
    currSum+=T[N-2][N-1]
    currSum+=T[N-1][N-2]
    if(currSum>maxSum):
        maxSum=currSum
        maxRow=N-1
        maxCol=N-1
    currSum=0

    #krawedzie
    #gora
    for col in range(1,N-1):
        currSum+=T[0][col-1]
        currSum+=T[0][col+1]
        currSum+=T[1][col-1]
        currSum+=T[1][col]
        currSum+=T[1][col+1]
        if(currSum>maxSum):
            maxSum=currSum
            maxRow=0
            maxCol=col
        currSum=0

    #dol
    for col in range(1,N-1):
        currSum+=T[N-1][col-1]
        currSum+=T[N-1][col+1]
        currSum+=T[N-2][col-1]
        currSum+=T[N-2][col]
        currSum+=T[N-2][col+1]
        if(currSum>maxSum):
            maxSum=currSum
            maxRow=N-1
            maxCol=col
        currSum=0

    #lewa
    for row in range(1,N-1):
        currSum+=T[row-1][0]
        currSum+=T[row+1][0]
        currSum+=T[row-1][1]
        currSum+=T[row][1]
        currSum+=T[row+1][1]
        if(currSum>maxSum):
            maxSum=currSum
            maxRow=row
            maxCol=0
        currSum=0

    #prawa
    for row in range(1,N-1):
        currSum+=T[row-1][N-1]
        currSum+=T[row+1][N-1]
        currSum+=T[row-1][N-2]
        currSum+=T[row][N-2]
        currSum+=T[row+1][N-2]
        if(currSum>maxSum):
            maxSum=currSum
            maxRow=row
            maxCol=N-1
        currSum=0

    #srodek
    for row in range(1,N-1):
        for col in range(1,N-1):
            currSum+=T[row-1][col-1]
            currSum+=T[row-1][col]
            currSum+=T[row-1][col+1]
            currSum+=T[row][col-1]
            currSum+=T[row][col+1]
            currSum+=T[row+1][col-1]
            currSum+=T[row+1][col]
            currSum+=T[row+1][col+1]
            if(currSum>maxSum):
                maxSum=currSum
                maxRow=row
                maxCol=col
            currSum=0

    return (maxSum,maxRow,maxCol)

def main():
    N=int(input("N: "))
    Tab=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(Tab,N)
    print_tab(Tab)
    print(maxNeiSum(Tab))

if __name__ == "__main__": main()