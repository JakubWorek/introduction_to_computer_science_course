#program generujący i wypisujący liczby pierwsze mniejsze od N 
#metodą Sita Eratostenesa.

from math import sqrt

maxwart=1000

def wypelnij_sito(tablica):
    tablica[0]=False
    tablica[1]=False

    for i in range(2,int(sqrt(maxwart))+1):
        if(tablica[i]==True):
            for j in range(2*i,maxwart+1,i): tablica[j]=False


def wypisz_sito(tablica,n):
    for i in range(0,n+1):
        if(tablica[i]==True):
            print(i)


def main():
    sito=[True for _ in range(maxwart+1)]
    wypelnij_sito(sito)
    wypisz_sito(sito,maxwart)

if __name__ == "__main__": main()