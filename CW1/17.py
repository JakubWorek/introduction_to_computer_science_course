#program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów
#ciągu Fibonacciego. Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu

#odp zmierza do złotej proporcji 1.61

def fib(x):
	#if(x<0): return
	#if(x==0): print(0); return
	#if(x==1): print(0); print(1); return

	previous = 0
	current = 1
	next = 0
	#print(0)
	#print(1)
	while(current+previous<x):
		next = current + previous
		print(next/current)
		previous = current
		current = next
		
	return

def main():
    fib(10000)
    

if __name__ == "__main__": main()