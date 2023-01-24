#Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
#według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
#czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
#możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
#skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.

from math import inf

def factors(n):
    factors = []
    for i in range(2, n+1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    
    return factors

def zadanie(T,N,i,cnt):
    #print(i)
    if i == N-1:
        #print("Git")
        #print(cnt)
        return cnt
    if i>N-1:
        return inf

    #print(T[i])
    factortab = factors(T[i])
    #print(factortab)

    best = inf
    
    for factor in factortab:
        #print(factor)
        best=min(best,zadanie(T,N,i+factor,cnt+1))

    if best != inf: return best
    return best


def main():
    T = [6,5,1,2,4,3]
    N=len(T)
    print(zadanie(T,N,0,0))


if __name__ == '__main__': main()
