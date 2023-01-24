#6. Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
#funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
#wartość.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def AtEnd(head,val):
    curr=head

    while curr.next is not None:
        curr = curr.next

    curr.next=Node(val)

    return