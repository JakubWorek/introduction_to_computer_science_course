#program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
#o najmniejszej różnicy

def rozkladNaIloczyn(a):
    min1=a
    min2=1
    f1=0
    f2=0

    for i in range(1,int(a**0.5)+1):
        if(a%i==0):
            f1=i
            f2=int(a/i)
        if(abs(f1-f2)<abs(min1-min2)): min1=f1; min2=f2

    print(min1, min2)
        

def main():
    a=int(input("podaj liczbe:"))
    rozkladNaIloczyn(a)

    

if __name__ == "__main__": main()