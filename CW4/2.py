#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
#z nieparzystych cyfr

from random import randint

def print_tab(tab):
    for line in tab:
        print(line)

def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,10)
    return T

def isOddCyf(num):
    while(num>0):
        cyf=num%10
        if(cyf%2==0): return False
        num//=10
    return True

def ex2(tab,n):
    for rows in range(n):
        flag=False
        for i in range(n):
            if(isOddCyf(tab[rows][i])): flag = True
        if(not flag): return False
    
    return True

def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)
    print(ex2(T,N))

if __name__ == "__main__": main()