#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
#poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
#narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
#czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu

from random import randint

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,9)
    return T


def isSqInT(T,N,k):
    for bok in range(3,N+1,2):
        print(bok)
        for RowS in range(1,N-bok//2):
            for ColS in range(1,N-bok//2):
                    iloczyn=1
                    iloczyn*=T[RowS-bok//2][ColS-bok//2] #lewa gora
                    iloczyn*=T[RowS-bok//2][ColS+bok//2] #prawa gora
                    iloczyn*=T[RowS+bok//2][ColS-bok//2] #lewy dol
                    iloczyn*=T[RowS+bok//2][ColS+bok//2] #prawy dol
                    if(iloczyn == k):
                        return (True,RowS,ColS)

    return False

    
def main():
    N=int(input("N: "))
    T1=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T1,N)
    print_tab(T1)
    K=int(input("K: "))
    print(isSqInT(T1,N,K))

if __name__ == "__main__": main()