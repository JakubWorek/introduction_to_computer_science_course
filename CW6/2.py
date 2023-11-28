#”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
#waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
#naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
#równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool

def waga(num):
    n=num
    cz=2 #potencjalny czynnik
    licz=0

    while(n>1):
        if(n%cz==0):
            licz+=1
            while(n%cz==0): 
                n=n//cz
        cz+=1

    return licz


def podzielT(T,n,i,s1,s2,s3):
    if(i == n):
        if(s1==s2 and s2==s3 and s3==s1):
            return True
        else: return False
    
    return podzielT(T,n,i+1,s1+waga(T[i]),s2,s3) or podzielT(T,n,i+1,s1,s2+waga(T[i]),s3) or podzielT(T,n,i+1,s1,s2,s3+waga(T[i]))


def main():
    T=[1,2,3,4,5]
    print(podzielT(T,len(T),0,0,0,0))

if __name__ == "__main__": main()
