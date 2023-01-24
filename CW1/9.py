# program wypisujący podzielniki liczby

def dzielniki(a):
    for i in range(1,int(a/2)+1):
        if(a%i==0): print(i)
    print(a)

def dzielnikip(a):
    for i in range(1,int(a**0.5)+1):
        if(a%i==0):
            print(i)
            if(a/i != i):
                print(int(a/i))

def main():
    liczba=int(input("Podaj liczbe ktorej dzielniki wyswietle:"))
    #dzielniki(liczba)
    dzielnikip(liczba)

if __name__ == "__main__": main()