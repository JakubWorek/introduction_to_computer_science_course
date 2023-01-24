#program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta zawiera cyfrę równą liczbie swoich cyfr

from math import log10

def czyCyfra(liczba):
    len=int(log10(liczba))+1

    while(liczba>0):
        cyf=liczba%10
        if(cyf==len): return True
        liczba//=10

    return False


def main():
    num=int(input("Podaj liczbe: "))
    print(czyCyfra(num))

if __name__ == "__main__": main()