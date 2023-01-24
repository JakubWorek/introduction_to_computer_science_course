#Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
#wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
#elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
#wartość sumy, funkcja powinna zwrócić wartość typu bool

from random import randint

N=8
T=[[0 for _ in range(N)] for _ in range(N)]

def print_tab(tab):
    for line in tab:
        print(line)

def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=randint(1,9)
    return T




def CanGetSum(T,sum):
    n=len(T)
    cols=[False for _ in range(n)]
    def rek(T,row,sum,curr,notEmpty,cols):
        #print(curr)
        if(row==len(T)):
            return(curr==sum and notEmpty)
        
        for col in range(len(T)):
            if(cols[col]==False):
                if(rek(T,row+1,curr,sum,notEmpty,cols)): return True
                cols[col]=True
                if(rek(T,row+1,curr+T[row][col],sum,True,cols)): return True
                cols[col]=False

        return False
    
    return rek(T,0,sum,0,False,cols)




def main():
    global T
    global N
    #wypelnij(T,N)
    T=[ [5, 5, 3, 7, 3, 1, 1, 6],
        [7, 6, 5, 9, 9, 8, 5, 3],
        [3, 7, 7, 4, 1, 3, 4, 6],
        [5, 5, 4, 3, 2, 6, 3, 7],
        [9, 3, 8, 7, 7, 1, 4, 8],
        [6, 6, 3, 2, 6, 8, 6, 1],
        [9, 9, 1, 4, 2, 4, 8, 3],
        [3, 5, 8, 7, 4, 1, 6, 5]  ]
    print_tab(T)
    print(CanGetSum(T,13))
    

if __name__ == "__main__": main()