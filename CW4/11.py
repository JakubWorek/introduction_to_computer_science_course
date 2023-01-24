#Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
#są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553. Dana jest tablica T[N][N] wypełniona liczbami
#naturalnymi. Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z
#przyjaciółkami

from random import randint

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,1)
    return T


def areFriends(num1,num2):
    tab=[False]*10

    while(num1>0):
        cyf=num1%10
        tab[cyf]=True
        num1//=10

    while(num2>0):
        cyf=num2%10
        if(tab[cyf]==False): return False
        num2//=10

    return True


def cntFriInT(T,N):
    if(N<2): return 0
    cnt=0
    
    #rogi
    if(
        areFriends(T[0][0],T[0][1])
        and areFriends(T[0][0],T[1][0])
        and areFriends(T[0][0],T[1][1])
    ): cnt+=1

    if(
        areFriends(T[0][N-1],T[0][N-2])
        and areFriends(T[0][N-1],T[1][N-2])
        and areFriends(T[0][N-1],T[1][N-1])
    ): cnt+=1

    if(
        areFriends(T[N-1][0],T[N-2][0])
        and areFriends(T[N-1][0],T[N-2][1])
        and areFriends(T[N-1][0],T[N-1][1])
    ): cnt+=1

    if(
        areFriends(T[N-1][N-1],T[N-2][N-2])
        and areFriends(T[N-1][N-1],T[N-2][N-1])
        and areFriends(T[N-1][N-1],T[N-1][N-2])
    ): cnt+=1

    #krawedzie
    #gora
    for col in range(1,N-1):
        if(
            areFriends(T[0][col],T[0][col-1])
            and areFriends(T[0][col],T[0][col+1])
            and areFriends(T[0][col],T[1][col-1])
            and areFriends(T[0][col],T[1][col])
            and areFriends(T[0][col],T[1][col+1])
        ): cnt+=1
    #dol
    for col in range(1,N-1):
        if(
            areFriends(T[N-1][col],T[N-1][col-1])
            and areFriends(T[N-1][col],T[N-1][col+1])
            and areFriends(T[N-1][col],T[N-2][col-1])
            and areFriends(T[N-1][col],T[N-2][col])
            and areFriends(T[N-1][col],T[N-2][col+1])
        ): cnt+=1
    #lewa
    for row in range(1,N-1):
        if(
            areFriends(T[row][0],T[row-1][0])
            and areFriends(T[row][0],T[row+1][0])
            and areFriends(T[row][0],T[row-1][1])
            and areFriends(T[row][0],T[row][1])
            and areFriends(T[row][0],T[row+1][1])
        ): cnt+=1
    #prawa
    for row in range(1,N-1):
        if(
            areFriends(T[row][N-1],T[row-1][N-1])
            and areFriends(T[row][N-1],T[row+1][N-1])
            and areFriends(T[row][N-1],T[row-1][N-2])
            and areFriends(T[row][N-1],T[row][N-2])
            and areFriends(T[row][N-1],T[row+1][N-2])
        ): cnt+=1
    #srodek
    for row in range(1,N-1):
        for col in range(1,N-1):
            if(
                areFriends(T[row][col],T[row-1][col-1])
                and areFriends(T[row][col],T[row-1][col])
                and areFriends(T[row][col],T[row-1][col+1])
                and areFriends(T[row][col],T[row][col-1])
                and areFriends(T[row][col],T[row][col+1])
                and areFriends(T[row][col],T[row+1][col-1])
                and areFriends(T[row][col],T[row+1][col])
                and areFriends(T[row][col],T[row+1][col+1])
            ): cnt+=1

    return cnt


def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)
    print(cntFriInT(T,N))

if __name__ == "__main__": main()
