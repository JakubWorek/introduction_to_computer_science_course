#program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
#nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
#znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością najdłuższego ciągu arytmetycznego
#o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych
#indeksach.


from random import randint

def wypelnij(T,N):
    for i in range(N):
        T[i]=randint(1,99)
    return T

def longestAritmetic(T,N):
    if(N<=1): return N

    max_leng_inc=1
    max_leng_dec=1
    leng=2
    r=T[1]-T[0]


    for i in range(2,N):
        if(T[i]-T[i-1]==r): leng+=1
        else:
            if(r<0):
                if(leng>max_leng_dec): max_leng_dec=leng
                leng=2
                r=T[i]-T[i-1]
            if(r>0):
                if(leng>max_leng_inc): max_leng_inc=leng
                leng=2
                r=T[i]-T[i-1]

    if(r<0):
        if(leng>max_leng_dec): max_leng_dec=leng
    if(r>0):
        if(leng>max_leng_inc): max_leng_inc=leng

    return max_leng_inc-max_leng_dec
    

def main():
    N=int(input("N: "))
    tab=[0 for _ in range(N)]
    wypelnij(tab,N)
    print(tab)
    print(longestAritmetic(tab,N))

if __name__ == "__main__": main()