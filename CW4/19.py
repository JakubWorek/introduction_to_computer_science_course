#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
#szachowego.

from random import randint
from math import isqrt

def print_tab(tab):
    for line in tab:
        print(line)

def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,9)
    return T


def skoczki(tab,k):
    moves = [(2, 1), (1, 2), (2, -1), (1, -2)]  # Ruchy skoczka tylko w dol szachownicy
    n = len(tab)
    counter = 0
    for row in range(n - 1):  # Kiedy patrze ruchami skoczka w dół, nie musze iterować do końca tablicy
        for col in range(n):
            for el in moves:
                rowSkocz, colSkocz = row + el[0], col + el[1]
                if rowSkocz < n and 0 <= colSkocz < n:
                    curr_num = tab[row][col] * tab[rowSkocz][colSkocz]
                    if curr_num == k:
                        counter += 1
    return counter

def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)

    il=int(input("Iloczyn: "))
    print(skoczki(T,il))

if __name__ == "__main__": main()