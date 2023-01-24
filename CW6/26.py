#Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A cyfr
#1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca ilość
#wszystkich możliwych do zbudowania liczb, takich że pierwsza cyfra w systemie dwójkowym 
#(najstarszy bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
#10010(2), 10100(2), 11000(2)

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


def rek(A,B,newNum=0):
    if(A==0 and B==0):
        if(not isPrime(newNum)): return 1
        return 0

    a,b=0,0

    if(A>0):
        a=rek(A-1,B,newNum+2**(A+B-1))
    
    if(B>0):
        b=rek(A,B-1,newNum)
    
    return a+b

def oneOnBeg(A,B):
    new=2**(A+B-1)
    return rek(A-1,B,new)

print(oneOnBeg(2,3))