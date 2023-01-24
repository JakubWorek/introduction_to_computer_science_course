#Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
#M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
#naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
#tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
#powinny zawierać zera

from random import randint

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnijRosnaco(T,N):
    for i in range(N):
        p1=0
        p2=100
        ilosc=N
        for j in range(N):
            T[i][j]=p1+(randint(1,1000)%int((p2-p1+1)/ilosc))
            ilosc-=1
            p1=T[i][j]
    return T


def isSingleton(T,N,num):
    flag=False

    for i in range(N):
        for j in range(N):
            if(T[i][j]==num and flag==False): flag=True
            elif(T[i][j]==num and flag==True): return False

    return True


def mergeSingletones(T1,T2,N):
    for row in range(N):
        ind=N*N-1
        for col in range(N-1,-1,-1):
            if(isSingleton(T1,N,T1[row][col])):
                while(T2[ind] > T1[row][col]): ind-=1
                for k in range(ind):
                    T2[k]=T2[k+1]
                T2[ind]=T1[row][col]

    return T2


def main():
    N=int(input("N: "))
    T1=[[0 for _ in range(N)] for _ in range(N)]
    T2=[0 for _ in range(N*N)]
    wypelnijRosnaco(T1,N)
    print_tab(T1)
    print(mergeSingletones(T1,T2,N))

if __name__ == "__main__": main()