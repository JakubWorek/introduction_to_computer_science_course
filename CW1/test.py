def czyMozna(tab,row,col):
    n=len(tab)
    if(tab[row][col]==0):
        for i in range(n):
            if(tab[row][i]!=0): return False
            if(tab[i][col]!=0): return False
        for x in range(-8,9,1):
            if(0<=row+x<4 and 0<=col+x<4):
                #print(row+x,col+x,"XD")
                if(tab[row+x][col+x]!=0): return False
            
    return True

T=[
    [0,0,1,1],
    [0,0,0,0],
    [1,0,0,1],
    [0,0,1,0],
    ]

print(czyMozna(T,1,1))