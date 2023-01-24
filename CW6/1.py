#Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
#co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
#cyfry

from math import isqrt


def isPrime(num):
    if(num<2): return False
    if(num==2 or num ==3): return True
    if(num%2==0 or num%3==0): return False

    i=5
    while(i<isqrt(num)+1):
        if(num%i==0): return False
        i+=2
        if(num%i==0): return False
        i+=4

    return True


def findPrimeSubNum(num,newNum=0,p=0,oneDigDel=False):
    #warunek końca, jeżeli num już się nie da podzielić (num==0)
    #to zwracamy (no i jeszcze jak ta nowa liczba jest git to ją wypisać)
    if num==0:
        if newNum>9 and isPrime(newNum) and oneDigDel:
            print(newNum)
        return
    #albo zmieniamy newNum dodając do niego ostatnią
    # cyfre z num na przód i skracamy num
    findPrimeSubNum(num//10,newNum+((num % 10) * (10 ** p)),p+1,oneDigDel)
    #albo nie zmieniamy newNum i skracamy num
    findPrimeSubNum(num//10,newNum,p,True)


def main():
    num=12345
    findPrimeSubNum(num)

if __name__ == "__main__": main()