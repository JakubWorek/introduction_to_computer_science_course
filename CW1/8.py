#program sprawdzający czy zadana liczba jest pierwsza

def czyPierwsza(x):
    if(x<2): return False
    i=2
    while(i*i<x):
        if(x%i==0): return False
        i+=1
    return True

def main():
    liczba=int(input("Podaj liczbe do sprawdzenia:"))
    if(czyPierwsza(liczba)): print("Podana liczba jest liczba pierwsza")
    else: print("Podana liczba nie jest liczba pierwsza")

if __name__ == "__main__": main()