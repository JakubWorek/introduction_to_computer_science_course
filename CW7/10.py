#10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
#funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
#powstać nowa lista. 

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


def push_back(l: Node, val: int):
    if l == None:
        return Node(val)


    while l.next != None:
        l = l.next
    
    l.next = Node(val)


def add(num1, num2):
    rev1=ReverseLinkedList(num1)
    rev2=ReverseLinkedList(num2)

    ans = Node()


    c1 = rev1
    c2 = rev2
    next_a = 0
    

    while c1 != None or c2 != None:
        v = next_a
        if c1 != None:
            v += c1.val
            c1 = c1.next
        if c2 != None:
            v += c2.val
            c2 = c2.next
        
        
        next_a = v // 10
        push_back(ans, v%10)



    if next_a != 0:
        push_back(ans, next_a)


    num = ReverseLinkedList(ans)
    
    return num