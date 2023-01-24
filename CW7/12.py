#Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci
#jednokierunkowej listy. Napisy w łańcuchu są uporządkowane
#leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
#dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy
#oraz wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą,
#czy w wyniku operacji moc zbioru uległa zmianie.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def Difference(str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i
    
    if len(str1) == len(str2):
        return -1
    
    return min(len(str1), len(str2))


def Insert(head, str):
    guard=Node()
    guard.next = head

    curr=guard
    while curr.next is not None:
        r=Difference(str, curr.next.val)
        if r==-1: #already in list
            return
        if r==len(curr.next.val): #not this time
            curr=curr.next
            continue
        if r==len(str) or ord(str[r])<ord(curr.next.val[r]):
            new=Node(str)
            new.next=curr.next
            curr.next=new
            return

        curr=curr.next
    
    if curr.val == str:
        return 
    curr.next=Node(str)