#Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale od 1
#do k, metodą trapezów

import math

def f(x):
    return 1/x

def main():
    n=10000 #liczba trapezow
    L=1.0; P=float(input("Podaj zakres: ")) #dziedzina
    p=0.0 #pole powierzchni pod wykresem
    x=L #bierzaca wartosc idaca
    w=(P-L)/n #szerokosc jednego trapezu

    for i in range(1,n+1):
        p=p+w*(f(x)+f(x+w))/2
        x=x+w

    print("Pole powierzchni pod wykresem:", round(p,4))

if __name__ == "__main__": main()