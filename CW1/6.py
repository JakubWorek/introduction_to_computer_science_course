#program rozwiązujący równanie x^x=2020 metoda bisekcji

def f(x) -> float:
    return (x**x)-2020

def main():
    L=4.8; P=5.0 #przedzial w ktorym szukamy miejsc zerowych
    e=0.000000001 #dokladnosc
    l=float(f(L))
    p=float(f(P))
    x=(l+p)/2

    #if(float(f(x))==0): print(x)
    #else:
    if(1==1):
        while(abs(l-p)>e):
            x=(l+p)/2
            if(float(f(l))*float(f(x))<0):
                p=x
            #if(float(f(x))*float(f(p))<0):
            else:
                l=x
        print((l+p)/2)

if __name__ == "__main__": main()