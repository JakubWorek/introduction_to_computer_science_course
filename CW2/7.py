#program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1

from math import sqrt

def szukaj(n):
    for i in range(1, int(sqrt(n))):
        an = i**2 + i + 1
        if n%an == 0:
            print("tak")
            break

    else:
        print("nie")
    

def main():
    liczba=int(input("podaj liczbe do sprawdzenia: "))
    szukaj(liczba)

if __name__ == "__main__": main()