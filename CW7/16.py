#Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
#początek listy jednokierunkowej, przenosi na początek listy te z nich,
#które mają parzystą ilość piątek w zapisie ósemkowym. 

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def CntIn8(num):
    counter = 0

    while num > 0:
        if num % 8 == 5: counter += 1
        num //= 8
    
    return counter%2==0

def Solve(head):
    guard=Node()
    guard.next = head

    if guard.next is None: return

    NextGuard=head
    curr=guard

    if CntIn8(curr.next.val):
        curr=curr.next

    while curr is not None and curr.next is not None:
        currVal=curr.next.val
        if CntIn8(currVal):
            guard.next=Node(currVal)
            guard.next.next=NextGuard
            NextGuard=guard.next
            curr.next=curr.next.next
        else:
            curr=curr.next


