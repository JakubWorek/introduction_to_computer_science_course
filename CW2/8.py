#Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego, np. 9,14,15,17,22. 
#Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje
#następną taką liczbę większą od n. Można założyć, że 0 < n < 1000

def zadanaSuma(zs):
	ss=0 #substring sum
	previous = 0
	current = 1
	next = 0

	while(current+previous<=zs and ss<=zs):
		ss+=current
		next = current + previous
		previous = current
		current = next
		if(ss==zs):
			return True


	previous = 0
	current = 1
	next = 1
	while(current+previous<=zs and ss>=zs):
		ss-=current
		next = current + previous
		previous = current
		current = next
		if(ss==zs):
			return True


	return False


def main():
	n=int(input("Podaj n: "))
	n+=1
	while(True):
		if(zadanaSuma(n)==False): print(n); break
		n+=1
		
if __name__ == "__main__": main()