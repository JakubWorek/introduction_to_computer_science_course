#program, który wypełnia N-elementową tablicę t trzycyfrowymi liczbami
#pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego 
#podciągu spójnego znajdującego się w tablicy dla którego w tablicy występuje
#również rewers tego ciągu. Na przykład dla tablicy: 
#t=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4

from random import randint

def wypelnij(T,N):
    for i in range(N):
        T[i]=randint(100,999)
    return T

def longestRevers(T,N):
    

def main():
    N=int(input("N: "))
    tab=[0 for _ in range(N)]
    wypelnij(tab,N)
    print(tab)
    print(longestRevers(tab,N))

if __name__ == "__main__": main()