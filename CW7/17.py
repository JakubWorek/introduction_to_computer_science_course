# Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
#początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
#wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek. 

class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


def CntIn8(num):
    counter = 0

    while num > 0:
        if num % 2 == 1: counter += 1
        num //= 2
    
    return counter%2==1

def Solve(head):
    guard=Node()
    guard.next = head

    if guard.next is None: return
    curr=guard

    while curr.next is not None:
        currVal=curr.next.val
        if CntIn8(currVal):
            if curr.next.next != None:
                curr.next.next.prev = curr
            curr.next=curr.next.next
        else:
            curr=curr.next