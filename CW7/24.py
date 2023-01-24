#Dana jest lista, który zakończona jest cyklem.
#Napisać funkcję, która zwraca liczbę elementów w cyklu.

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