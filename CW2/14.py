#Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą wystąpić 
#wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
#wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
#75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
#zadanych liczb.

from math import isqrt
from math import log10

def isPrime(x):
    if(x==2 or x==3): return True
    if(x%2==0 or x%3==0 or x<=1): return False
    i=5

    while(i<isqrt(x)+1):
        if(x%i==0): return False
        i+=2
        if(x%i==0): return False
        i+=4

    return True


def leng(num):
    return int(log10(num)) + 1


def validateMask(num1:int,num2:int,mask:int):
    cnt1=leng(num1)
    cnt2=leng(num2)

    while(mask>0):
        if(mask%2==0): cnt1-=1
        else: cnt2-=1
        mask//=2

    return (cnt1>=0 and cnt2==0) #true or false


def mixNums(num1:int,num2:int,mask:int):
    newNum=0
    mult=1
    while(mask>0 or num1>0):
        if(mask%2==0):
            d=num1%10
            num1//=10
        else:
            d=num2%10
            num2//=10
        
        mask//=2
        newNum+=d*mult
        mult*=10

    return newNum


def main():
    l1=int(input("l1: "))
    l2=int(input("l2: "))

    cnt = 0
    leng_l1, leng_l2 = leng(l1), leng(l2)

    for mask in range(2**(leng_l1 + leng_l2)):
        if validateMask(leng_l1, leng_l2, mask) and isPrime(mixNums(l1, l2, mask)):
            cnt += 1

    print(cnt)


if __name__ == "__main__": main()