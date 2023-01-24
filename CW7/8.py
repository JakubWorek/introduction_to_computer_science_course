#Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
#element listy. Do funkcji należy przekazać wskazanie na pierwszy element
#listy.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def Del2(head):
    curr=head

    while curr.next is not None:
        tmp = curr.next.next
        del curr.next
        curr.next = tmp

        if curr.next is not None:
            curr = curr.next
