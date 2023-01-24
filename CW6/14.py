#Problem wież w Hanoi (treść oczywista)

def przenies(p,q):
    palik=['a','b','c']
    print(palik[p], "->", palik[q])

def hanoi(n:int,a:int,b:int,c:int):
    if(n > 1): hanoi(n - 1, a, c, b)
    przenies(a, c)
    if(n > 1): hanoi(n - 1, b, a, c)

def main():
    print("Wieze Hanoi")
    n=int(input("Podaj liczbe krazkow:"))
    hanoi(n, 0, 1, 2)

if __name__ == "__main__": main()