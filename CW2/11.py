#program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#jej cyfry stanowią ciąg rosnący

def czyRosnacy(liczba):
    cyf=liczba%10
    liczba//=10
    while(liczba>0):
        if(cyf<=liczba%10): return False
        cyf=liczba%10
        liczba//=10

    return True


def main():
    num=int(input("Podaj liczbe: "))
    print(czyRosnacy(num))

if __name__ == "__main__": main()