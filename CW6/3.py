#Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie
#k. Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
#koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na
#polu startowym i ostatnim także wliczamy do kosztu przejścia.

from random import randint


def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,9)
    return T


#krol moze poruszac sie w 3 strony: k-1,k,k+1 gdzie k to kolumna
def koszt(row,col,T):
    if(row==7): return T[row][col]
    
    if(col>0):
        left=koszt(row+1,col-1,T)
    else:
        left=float('inf')

    if(col<7):
        right=koszt(row+1,col+1,T)
    else:
        right=float('inf')
    
    middle=koszt(row+1,col,T)

    return min(left,middle,right)+T[row][col]


def main():
    N=8
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print_tab(T)
    print(koszt(0,0,T))
    

if __name__ == "__main__": main()