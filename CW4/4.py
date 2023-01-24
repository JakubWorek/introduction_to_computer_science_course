#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
#element do sumy elementów wiersza w którym leży element jest największa.

from random import randint

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,100)
    return T


def calcColAndRowSum(tab):
    colSums = [0]*len(tab)
    rowSums = [0]*len(tab)

    for x in range(len(tab)):
        for y in range(len(tab)):
            colSums[x] += tab[y][x]
            rowSums[y] += tab[y][x]
        
    return rowSums, colSums


def ex4(tab):
    rowS,colS=calcColAndRowSum(tab)

    maxCol=max(colS)
    indMaxCol=colS.index(maxCol)

    minRow=min(rowS)
    indMinRow=rowS.index(minRow)

    return maxCol/minRow,indMaxCol,indMinRow
    

def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)
    print(ex4(T))

if __name__ == "__main__": main()