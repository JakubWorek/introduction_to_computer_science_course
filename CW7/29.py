#Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
#naturalne. W obu listach liczby są posortowane rosnąco. Proszę napisać
#funkcję usuwającą z każdej listy liczby nie występujące w drugiej. Do
#funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
#łączną liczbę usuniętych elementów. 

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def inList(lst, val):
    if lst.val == None:
        lst = lst.next
    
    while lst != None and lst.val < val:
        lst = lst.next

    return lst != None and lst.val == val

def remove(lst1, lst2):
    cnt=0
    while lst1.next is not None:
        if not inList(lst2, lst1.next.val):
            lst1.next = lst1.next.next
            cnt+=1
        else:
            lst1=lst1.next
    return cnt

def solve(l1,l2):
    return remove(l1,l2)+remove(l2,l1)
