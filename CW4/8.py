#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
#poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
#co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
#się znaleźć taki ciąg oraz długość tego ciągu

from random import randint

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,100)
    return T


def lenOfLongGeomSubseq(T,N):
    if(N < 3): return False

    maxLeng=1

    for col in range(N-2):
        q=T[1][col+1]/T[0][col]
        leng=2

        for row in range(2,N-col):
            if(T[row][col+row] == T[row-1][col+row-1]*q): leng+=1
            else:
                maxLeng=max(maxLeng,leng)
                leng=2
                q=T[row][col+1]/T[row-1][col+row-1]

        maxLeng=max(maxLeng,leng)

    
    for row in range(N-2):
        q=T[row+1][1]/T[row][0]
        leng=2

        for col in range(2,N-row):
            if(T[row+col][col] == T[row+col-1][col-1]*q): leng+=1
            else:
                maxLeng=max(maxLeng,leng)
                leng=2
                q=T[row+1][col]/T[row+col-1][col-1]

        maxLeng=max(maxLeng,leng)

    return maxLeng if maxLeng>2 else False


def main():
    N=int(input("N: "))
    T1=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T1,N)
    print_tab(T1)
    print(lenOfLongGeomSubseq(T1,N))

if __name__ == "__main__": main()