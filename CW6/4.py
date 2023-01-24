#Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
#wymiarach NxN ruchem skoczka szachowego.

def print_tab(tab):
    for line in tab:
        print(line)


def wypelnij(T,N):
    for i in range(N):
        for j in range(N):
            T[i][j]=0
    return T


def contains(T,w,k):
    if 0<=w<len(T) and 0<=k<len(T):
        return True
    return False


def knightWalk(T,row=0,col=0,n=1):
    T[row][col]=n
    if n == len(T)**2: return True

    jumps=[(1, 2), (-1, 2), (1, -2), (-1, -2),
            (2, 1), (2, -1), (-2, 1), (-2, -1)]

    for jump in jumps:
        nextRow=row+jump[0]
        nextCol=col+jump[1]

        if(contains(T,nextRow,nextCol) and T[nextRow][nextCol]==0):
            if(knightWalk(T,nextRow,nextCol,n+1)):
                return True
    
    T[row][col]=0
    return False


def main():
    N=int(input("N:"))
    T=[[0 for _ in range(N)] for _ in range(N)]
    wypelnij(T,N)
    print(knightWalk(T))
    print_tab(T)

    

if __name__ == "__main__": main()