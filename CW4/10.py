#Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
#True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
#False w przeciwnym przypadku.

from random import randint

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(0,2)
    return T


def is0InEvRoACoT(T,N):
    tab=[False]*N
    for row in T:
        for el in range(N):
            if(row[el]==0): tab[el]=True

    for i in range(N):
        if(tab[i]==False): return False

    return True

    
def main():
    N=int(input("N: "))
    T1=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T1,N)
    print_tab(T1)
    print(is0InEvRoACoT(T1,N))

if __name__ == "__main__": main()