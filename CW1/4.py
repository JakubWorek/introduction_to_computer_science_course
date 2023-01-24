#program obliczajacy pierwiastek całkowitoliczbowy z liczby naturalnej
#korzystając z zależności 1 + 3 + 5 + ... = n^2

def pierwiastek(x2):
    n=1 #wspolczynnik do sumy
    suma=0
    liczba=0

    while(suma<=x2):
        suma=suma+n
        liczba+=1
        n+=2

    print(liczba-1)

def main():
    n2=int(input("Podaj n^2: "))
    pierwiastek(n2)

if __name__ == "__main__": main()