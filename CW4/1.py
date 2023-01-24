#Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
#naturalnymi po spirali

from time import sleep

def print_tab(tab):
    for line in tab:
        print(line)

def main():
    N=int(input("N: "))
    T=[[0 for _ in range(N)] for _ in range(N)]
    
    x,y=0,0
    xi,yi=1,1
    i=1
    maxi=N*N
    print(maxi)

    while(i<=maxi):
        #w prawo
        while (x < N-1 and T[y][x+1]==0):
            T[y][x]=i
            x+=1
            i+=1
        
        print_tab(T)
        print(i)
        print("------")
        sleep(1)

        #w dół
        while (y < N-1 and T[y+1][x]==0):
            T[y][x]=i
            y+=1
            i+=1

        print_tab(T)
        print(i)
        print("------")
        sleep(1)

        #w lewo
        while (x > 0 and T[y][x-1]==0):
            T[y][x]=i
            x-=1
            i+=1

        print_tab(T)
        print(i)
        print("------")
        sleep(1)

        #w górę
        while (y > 0 and T[y-1][x]==0):
            T[y][x]=i
            y-=1
            i+=1

        print_tab(T)
        print(i)
        print("-----")
        sleep(1)

        if(i==maxi):
            T[y][x]=i
            i+=1

    print_tab(T)

if __name__ == "__main__": main()