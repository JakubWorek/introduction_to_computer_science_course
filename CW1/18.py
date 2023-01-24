#program wyznaczający pierwiastek sześcienny ze wzoru Newtona

def newton_sqrt(n):
    a = n/2
    e=0.0000001

    while(abs((n/(a*a))-a)>e):
        a=(a+(n/(a*a)))/2

    return a
	
def main():
    n=float(input("Podaj n: "))
    print(newton_sqrt(n))

if __name__ == "__main__": main()