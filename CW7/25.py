#Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
#zwraca wskaźnik do ostatniego elementu przed cyklem.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def lenB4Cycle(pointer):
    cnt = 0
    fast=pointer
    slow=pointer

    while True:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: break

    fast = pointer

    while fast != slow:
        fast = fast.next
        slow = slow.next
        cnt += 1

    return cnt

def getPtrB4Cycle(pointer):
    l=lenB4Cycle(pointer)
    l-=1
    if l<0: return None

    temp = pointer
    while l>0:
        l-=1
        temp=temp.next

    return temp