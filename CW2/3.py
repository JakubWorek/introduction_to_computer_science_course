#program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym

def czyPalindrom(a):
    a=str(a)
    i=0 
    j=len(a)-1

    while(i<j):
        if(a[i] != a[j]): return False
        i+=1
        j-=1

    return True


def decToBin(a):
    wynik=""

    while(a>0):
        if(a%2==1): wynik="1"+wynik
        else: wynik = "0" + wynik
        a=a//2
    
    return wynik


def main():
    liczba=int(input("podaj liczbe:"))
    print(czyPalindrom(liczba))
    print(czyPalindrom(decToBin(liczba)))

if __name__ == "__main__": main()