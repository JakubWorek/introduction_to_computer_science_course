zs=int(input("zs:"))
ss=0 #substring sum
previous = 0
current = 1
next = 0
flaga=0
while(current+previous<=zs and ss<=zs):
	print("curr",current)
	ss+=current
	next = current + previous
	previous = current
	current = next
	print("ss",ss)
	if(ss==zs):
		print("TAK")
		flaga=1
		break

previous = 0
current = 1
next = 1
while(current+previous<=zs and ss>=zs and flaga != 1):
	print("curr",current)
	ss-=current
	next = current + previous
	previous = current
	current = next
	print("ss",ss)
	if(ss==zs):
		print("TAK")
		flaga=1
		break
    
if (flaga != 1):
	print("NIE")
