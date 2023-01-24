#Dana jest tablica T[N][N] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy jako
#liczbę zapisaną w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000. Proszę zaimplementować funkcję distance(T), która dla takiej tablicy wyznaczy dwa wiersze, dla których różnica zawartych
#w wierszach liczb jest największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość
#pomiędzy znalezionymi wierszami. Można założyć, że żadne dwa wiersze nie zawierają identycznego ciągu
#cyfr.


def findMax(T):
    N=len(T)
    max=0
    posMax=-1

    for row in range(N):
        num=0
        n=N-1
        i=0

        while(n>-1):
            num+=(T[row][i])*(10**n)
            i+=1
            n-=1

        if(num>max):
            max=num
            posMax=row

    return posMax

    
def findMin(T):
    N=len(T)
    min=float('inf')
    posMin=-1

    for row in range(N):
        num=0
        n=N-1
        i=0

        while(n>-1):
            num+=(T[row][i])*(10**n)
            i+=1
            n-=1

        if(num<min):
            min=num
            posMin=row

    return posMin


def distance(tab):
    posMax=findMax(tab)
    posMin=findMin(tab)

    return(abs(posMin-posMax))


T = [
    [1,0,0,0,1,1,1,0],
    [1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0],
    [0,0,0,0,1,0,1,0],
    [1,0,0,0,1,1,1,1],
    [1,1,0,1,1,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1]
]
    
print(distance(T))