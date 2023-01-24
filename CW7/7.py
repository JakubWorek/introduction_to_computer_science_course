#Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
#należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def DelEnd(head):
    curr=head
    prev=head

    while curr.next is not None:
        prev=curr
        curr = curr.next

    prev.next=None

    return