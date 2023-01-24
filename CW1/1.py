#program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.

def fib(x):
	if(x<0): return
	if(x==0): print(0); return
	if(x==1): print(0); print(1); return

	previous = 0
	current = 1
	next = 0
	print(0)
	print(1)
	while(current+previous<x):
		next = current + previous
		print(next)
		previous = current
		current = next
		
	return

def main():
    fib(1000000)

if __name__ == "__main__": main()