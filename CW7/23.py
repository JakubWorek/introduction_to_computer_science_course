#Dana jest lista, który zakończona jest cyklem.
#Napisać funkcję, która zwraca liczbę elementów w cyklu.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def lenOfCycle(pointer):
    cnt = 0
    fast=pointer
    slow=pointer

    while True:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: break

    fast = fast.next.next
    slow = slow.next
    cnt += 1

    while fast != slow:
        cnt += 1
        fast = fast.next.next
        slow = slow.next

    return cnt