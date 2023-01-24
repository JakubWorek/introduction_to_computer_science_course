#Proszę znaleźć wyrazy początkowe zamiast 1,1 o najmniejszej sumie, aby w ciągu analogicznym
# do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.

def testfib(target):
	resA=0
	resB=0
	best=target

	for a in range(1,int(target/2)+2):
		for b in range(1,int(target/2)+2):
			prev=a
			curr=b
			while(prev+curr<target+2):
				next=prev+curr
				if(prev+curr==target):
					print(a, b)
					if(a+b<best):
						best=a+b
						resA=a
						resB=b
				prev=curr
				curr=next

	print(resA, ",", resB)
	
def main():
    testfib(2022)

if __name__ == "__main__": main()