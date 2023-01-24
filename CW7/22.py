#Dana jestlista, który być może zakończona jest cyklem.
#Napisać funkcję, która sprawdza ten fakt

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def hasCycle(pointer):
    fast=pointer
    slow=pointer
    while fast.next is not None\
        and fast.next.next is not None:
        if fast == slow and fast != pointer:
            return True
        fast = fast.next.next
        slow = slow.next
    return False