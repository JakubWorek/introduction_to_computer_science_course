#program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie.
fib:list=[]

def genfib(x):
	if(x<0): return
	if(x==0): fib.append(0); return
	if(x==1): fib.append(0); fib.append(1); return

	previous = 0
	current = 1
	next = 0
	fib.append(0)
	while(current + previous<x):
		next = current + previous
		fib.append(next)
		previous = current
		current = next
		
	return

def testsum(x):
    print(fib)
    for i in range(0,len(fib)):
        suma=0
        for j in range(i,len(fib)):
            suma=suma+fib[j]
            print(suma, fib[j])
            if(suma==x): print("TAK"); return
        
    print("NIE"); return

def main():
    n=int(input("Podaj zadana sume: "))
    genfib(n)
    testsum(n)

if __name__ == "__main__": main()