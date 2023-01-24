#Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
#z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
#sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole

from random import randint

def wypelnij(T,N):
    for i in range(N):
        T[i]=randint(1,10)
    return T

def checktab(T,N):
    helper=[False for _ in range(N)]
    helper[0]=True

    for i in range(N):
        if(helper[i]):
            num=T[i]
            div=2

            while(num>1):
                while(num%div==0):
                    if(i+div<N):
                        helper[i+div]=True
                    num//=div
                div+=1

    print(helper)

    return helper[N-1]

def main():
    N=int(input("N: "))
    tab=[0 for _ in range(N)]
    wypelnij(tab,N)
    print(tab)
    print(checktab(tab,N))

if __name__ == "__main__": main()