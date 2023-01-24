#Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami 
#naturalnym wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.

from random import randint

def wypelnij(T,N):
    for i in range(N):
        T[i]=randint(1,10)
    return T

def longestAritmetic(T,N):
    if(N<=1): return N

    max_leng=1
    leng=2
    r=T[1]-T[0]


    for i in range(2,N):
        if(T[i]-T[i-1]==r): leng+=1
        else:
            if(leng>max_leng): max_leng=leng
            leng=2
            r=T[i]-T[i-1]

    return max(max_leng,leng)
    

def main():
    N=int(input("N: "))
    tab=[0 for _ in range(N)]
    wypelnij(tab,N)
    print(tab)
    print(longestAritmetic(tab,N))

if __name__ == "__main__": main()