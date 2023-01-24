#Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
#Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
#napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
#Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
#powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]

class Node_pair:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b
        self.next = None

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def create_sum_list(head):
    ans=Node()
    start = head
    while head is not None:
        curr = ans
        while curr.next != None and curr.next.val <=head.a:
            curr=curr.next

        if curr.next == None:
            for i in range(head.a, head.b+1):
                curr.next = Node(i)
                curr=curr.next
        else:
            for i in range(head.a, head.b+1):
                if curr.next.val <= i: break
                new = Node(i)
                new.next=curr.next
                curr.next=new

                curr=curr.next
            
        head=head.next
    return ans

def shrink(p):
    head = p
    ans = Node_pair()
    curr_ans = ans

    start = head.next.val
    head=head.next

    while head.next is not None:
        if head.next.val != head.val + 1:
            curr_ans.next = Node_pair(start, head.val)
            start = head.next.val
            curr_ans=curr_ans.next
        head = head.next

    curr_ans = Node_pair(start, head.val)
    return ans 

# a - llista => b=create_sum_list(a) => shrink(b)