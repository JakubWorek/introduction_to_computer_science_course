#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
#parzystą.


from random import randint

def print_tab(tab):
    for line in tab:
        print(line)

def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,10)
    return T

def isEvenCyf(num):
    flag=False
    while(num>0):
        cyf=num%10
        if(cyf%2==0): flag=True
        num//=10

    if(flag): return True
    else: return False

def ex3(tab,n):
    booltab=[False for _ in range(n)]
    for rows in range(n):
        flag = False
        for i in range(n):
            if(isEvenCyf(tab[rows][i])): flag = True
        if(flag): booltab[rows]=True
    
    for i in range(n): 
        if(booltab[i]): return True

    return False

def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)
    print(ex3(T,N))

if __name__ == "__main__": main()