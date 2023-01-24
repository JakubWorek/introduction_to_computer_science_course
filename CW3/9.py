#Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
#długość najdłuższego, spójnego podciągu rosnącego

from random import randint

def wypelnij(T,N):
    for i in range(N):
        T[i]=randint(1,10)
    return T

def subros(T,N):
    if(N<=1): return N

    max_leng=1
    leng=1

    for i in range(1,N):
        if(T[i-1]<T[i]): leng+=1
        else:
            if(leng>max_leng): max_leng=leng
            leng=1

    return max_leng
    

def main():
    N=int(input("N: "))
    tab=[0 for _ in range(N)]
    wypelnij(tab,N)
    print(tab)
    print(subros(tab,N))

if __name__ == "__main__": main()