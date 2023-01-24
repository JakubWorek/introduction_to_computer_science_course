#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz
#jest równy 2

# an=3a(n-1)+1
# a(n+1)=9a(n-1)+4

def AodN(an):
    return 3*an+1

def jakasfunkcja(liczba):
    a=2
    while(a<=liczba):
        a=AodN(a)
        if(liczba%a==0): return True

    return False

def main():
    liczba=int(input("Podaj liczbe:"))
    print(jakasfunkcja(liczba))

if __name__ == "__main__": main()