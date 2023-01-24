#4. Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
#kolejność jej elementów.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def ReverseLinkedList(head):
    curr=head
    prev = None

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev