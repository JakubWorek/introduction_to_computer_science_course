#problem 8 hetmanów

def print_tab(tab):
    for line in tab:
        print(line)



def czyMozna(tab,row,col):
    n=len(tab)
    if(tab[row][col]!=0): return False
    if(tab[row][col]==0):
        for i in range(n):
            if(tab[row][i]!=0): return False
            if(tab[i][col]!=0): return False
        for x in range(-8,9,1):
            if(0<=row+x<n and 0<=col+x<n):
                if(tab[row+x][col+x]!=0): return False
            if(0<=row+x<n and 0<=col-x<n):
                if(tab[row+x][col-x]!=0): return False
    return True



def rek(ile,solution,curr=1):
    n=len(solution)
    if(ile==0): return True
    for x in range(n):
        for y in range(n):
            if(czyMozna(solution,x,y)):
                solution[x][y]=curr
                if(rek(ile-1,solution,curr+1)): return True
                solution[x][y]=0
    return False



def main():
    n=8
    solution=[[0 for _ in range(n)] for _ in range(n)]
    rek(n,solution)
    print_tab(solution)
    exit()
    
if __name__ == "__main__": main()