#Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
#wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
#75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
#zadanych liczb.

from math import isqrt
from math import log10

def isPrime(n):
    if(n<2): return False
    if(n%2==0 or n%3==0): return False
    if(n==2 or n==3): return True

    i=5
    while(i<isqrt(n)):
        if(n%i==0): return False
        i+=2
        if(n%i==0): return False
        i+=4

    return True


def leng(n):
    return int(log10(n))+1

def rev(n):
    sol = 0
    i = 0
    while n > 0:
        sol = sol * 10 + n % 10
        n //= 10
        i += 1
    return sol


def f(l1,l2):
    l1=rev(l1)
    l2=rev(l2)
    def rek(curr,l1,l2,cnt):
        if(l1==0 and l2==0):
            print(curr)
            if(isPrime(curr)): return 1
            return 0

        if(l1==0): return rek(curr*10+l2%10,l1,l2//10,cnt+1)
        if(l2==0): return rek(curr*10+l1%10,l1//10,l2,cnt+1)

        return rek(curr*10+l2%10,l1,l2//10,cnt+1)+rek(curr*10+l1%10,l1//10,l2,cnt+1)

    return rek(0,l1,l2,1)

print(f(123,75))