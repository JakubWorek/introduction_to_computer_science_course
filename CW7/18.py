#Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
#unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def Solve(head):
    guard=Node()
    guard.next = head
    uniq=Node()
    uniqNextGuard=uniq

    ll1 = guard.next
    while ll1 is not None:
        ll2 = guard.next
        test = True
        while ll2 is not None:
            if ll1==ll2:
                ll2=ll2.next
                continue
            if ll1.val==ll2.val:
                test = False
                break
            ll2=ll2.next
        
        if test == True:
            uniq.next=Node(ll1.val)
            uniq.next.next=uniqNextGuard
            uniqNextGuard=uniq.next
        
        ll1=ll1.next
    guard.next=uniq.next

    return guard
