#Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
#element listy o wartościach typu int, usuwającą wszystkie elementy, których
#wartość jest mniejsza od wartości bezpośrednio poprzedzających je
#elementów. 

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def Delete(head):
    curr=head
    lastVal=curr.val

    while curr.next.next is not None:
        currVal=curr.next.val

        if currVal < lastVal:
            currVal=curr.next.next.val
            curr.next=curr.next.next

        lastVal = currVal
        curr=curr.next

    if curr.next.val < lastVal:
        curr.next=None