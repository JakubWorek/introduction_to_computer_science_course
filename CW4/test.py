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


def mergeSingletones(T1,T2,N):
    for row in range(N):
        ind=N*N-1
        for col in range(N):
            print(T1[row][col])
            while(T2[ind] >= T1[row][col]): ind-=1
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