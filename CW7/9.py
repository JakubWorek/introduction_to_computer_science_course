#Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
#elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
#zwiększającą taką liczbę o 1.

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def ReverseLinkedList(head):
    curr=head
    prev = None

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


def AddOne(head):
    curr=ReverseLinkedList(head)

    while curr != None:
        if curr.val != 9 and curr.val != None:
            val=curr.val
            val+=1
            curr.val = val
            break
        else:
            curr.val = 0
            print(curr.val)
        
        if curr.next is None and curr.val == 0:
            curr.next = Node(1)
        curr=curr.next

    curr=ReverseLinkedList(curr)
    c=curr
    while c != None:
        print(c.val)
        c=c.next


z=Node(9)
x=Node(2,z)
y=Node(1,x)
curr=AddOne(y)



