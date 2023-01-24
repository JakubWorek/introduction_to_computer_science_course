#program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego

def czyFibonacci(a):
    if(a==0): return True
    if(a==1): return True

    f0=0; f1=1
    while (f0+f1<=a):
        next=f0+f1
        if(next==a): return True
        f0=f1
        f1=next

    return False

def main():
    a=int(input("podaj liczbe:"))
    for i in range(1,int(a**0.5)+1):
        if(a%i==0):
            if(czyFibonacci(i)==True):
                if(a/i != i):
                    if(czyFibonacci(int(a/i))==True):
                        print("Liczba jest iloczynem: ", i, int(a/i))

    

if __name__ == "__main__": main()