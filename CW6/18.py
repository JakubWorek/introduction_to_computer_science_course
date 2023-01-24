#W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
#nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
#polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
#(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
#T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
#w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
#narożnika.

from random import randint

N=8
T=[[0 for _ in range(N)] for _ in range(N)]

def print_tab(tab):
    for line in tab:
        print(line)

def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(100,999)
    return T


def isOnBoard(x,y,n):
    return 0<=x<n and 0<=y<n

def canMoveTo(fromX,fromY,x,y):
    return (fromX <= x and fromY <= y)

def getFirst(n):
    while(n//10 > 0): n//=10
    return n%10

def getLast(n):
    return n%10


def CanGetTo(T,x,y):
    if(x==7 and y==7): return True

    for i,j in [(1,1),(1,0),(0,1)]:
        if((canMoveTo(x,y,x+i,y+j)) and isOnBoard(x+i,y+j,8)):
            if(getLast(T[x][y])<getFirst(T[x+i][y+j])):
                return CanGetTo(T,x+i,y+j)

    return False



def main():
    global T
    global N
    wypelnij(T,N)
    print_tab(T)
    print(CanGetTo(T,0,4))
    

if __name__ == "__main__": main()
