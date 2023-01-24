#Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż
#2,3,5. Jedynka też jest taką liczbą. Napisz program, który wylicza ile takich liczb znajduje się w przedziale
#od 1 do N włącznie

def rozklad235(liczba):
    for cz in range(5,1,-1):
        while(liczba%cz==0): 
            liczba=liczba//cz
    
    if(liczba > 1): return False
    if(liczba == 1): return True


def main():
    n=int(input("podaj do jakiej liczby sprawdzać:"))

    for i in range(1,n+1):
        if(rozklad235(i)): print(i)

    

if __name__ == "__main__": main()