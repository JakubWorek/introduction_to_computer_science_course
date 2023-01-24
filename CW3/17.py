#Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w obu
#tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element (z
#tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
#sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
#i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
#tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.

from random import randint
from math import isqrt

def wypelnij(T):
    for i in range(len(T)):
        T[i]=randint(1,10)
    return T

def isPrime(num):
    if(num==2 or num ==3): return True
    if(num%2==0 or num%3==0): return False

    i=5
    while(i<isqrt(num)+1):
        if(num%i==0): return False
        i+=2
        if(num%i==0): return False
        i+=4

    return True


def sum(T1,T2,mask):
    suma=0

    for i in range(len(T1)):
        if(mask[i]==0): suma+=T1[i]
        if(mask[i]==1): suma+=T2[i]
        if(mask[i]==2): suma+=T1[i]; suma+=T2[i]

    return suma


def dec_to_tri(num,t1):
    nib=[0]*len(t1)

    for i in range(len(nib)-1,-1,-1):
        nib[i]=num%3
        num//=3

    return nib


def z17(T1,T2):
    cnt=0

    for mask in range(3**len(T1)):
        s=sum(T1,T2,dec_to_tri(mask,T1))
        if(isPrime(s)): cnt+=1

    return cnt


def main():
    N=int(input("N: "))
    tab1=[0 for _ in range(N)]
    tab2=[0 for _ in range(N)]
    wypelnij(tab1)
    wypelnij(tab2)
    print(tab1)
    print(tab2)
    print(z17(tab1,tab2))
    

if __name__ == "__main__": main()