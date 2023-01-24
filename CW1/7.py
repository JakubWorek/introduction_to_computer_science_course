#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego

fib:list=[]

def genfib(x):
	if(x<0): return
	if(x==0): fib.append(0); return
	if(x==1): fib.append(0); fib.append(1); return

	previous = 0
	current = 1
	next = 0
	fib.append(0)
	while(current<x):
		next = current + previous
		fib.append(current)
		previous = current
		current = next
		
	return

def testil(x):
    print(fib)
    for i in range(0,len(fib)-1):
        il=fib[i]*fib[i+1]
        if(il==x): print("TAK"); return
        
    print("NIE"); return

def main():
    n=int(input("Podaj zadany iloczyn: "))
    genfib(n)
    testil(n)

if __name__ == "__main__": main()