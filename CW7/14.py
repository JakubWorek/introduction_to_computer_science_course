#Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
#element listy o wartościach typu int, usuwającą wszystkie elementy, których
#wartość dzieli bez reszty wartość bezpośrednio następujących po nich
#elementów. 

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

    
def Delete(head):
    curr=head
    while curr.next is not None and\
         curr.next.next is not None:
        currVal=curr.next.val
        nextVal=curr.next.next.val

        if nextVal%currVal==0:
            curr.next=curr.next.next
        else:
            curr=curr.next