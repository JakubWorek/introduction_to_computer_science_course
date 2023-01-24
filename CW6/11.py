#Dana jest tablica T[N]. 
#Proszę napisać program zliczający liczbę “enek” o 
#określonym iloczynie.

def iloczyn(T,r,il,i,suma):
    if(r==il and suma>0): return 1
    if(r<=0 or i>=len(T)): return 0

    cnt=0
    cnt+=iloczyn(T,r*T[i],il,i+1,suma+1)
    cnt+=iloczyn(T,r,il,i+1,suma)

    return cnt


def main():
    global ile
    ilocz=12
    T=[1,2,3,4,5,6]
    print(iloczyn(T,1,ilocz,0,0))
    #print(ile)

if __name__ == "__main__": main()