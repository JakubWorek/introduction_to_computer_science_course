#program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba zakończona jest unikalną cyfrą

#from math import log10

def czyCyfraUnikalna(liczba):
    #len=int(log10(liczba))+1
    ost=liczba%10
    liczba//=10

    while(liczba>0):
        cyf=liczba%10
        if(cyf==ost): return False
        liczba//=10

    return True


def main():
    num=int(input("Podaj liczbe: "))
    print(czyCyfraUnikalna(num))

if __name__ == "__main__": main()