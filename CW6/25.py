#to samo co 22

from queue import PriorityQueue

def dzielniki(n):
    factors = []
    for i in range(2, n+1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    
    return factors

def fun(T):
    n=len(T)
    bad=[False for _ in range(n)]
    dp=[[] for _ in range(n)]

    for i in range(n):
        T[i]=dzielniki(T[i])
        for el in T[i]:
            if el+i<n:
                dp[el+i].append(i)
    
    kolejka=PriorityQueue()
    for el in dp[n-1]:
        kolejka.put(el,1)
    
    while not kolejka.empty():
        a,k=kolejka.get()
        if a==0: return k
        if not bad[a]:
            for idx in dp[a]:
                if not bad[idx]:
                    kolejka.put((a,idx))
        bad[a]=True
    
    return False
