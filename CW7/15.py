#Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
#początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
#wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek. 

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def CntIn3(num):
    counter = [0]*3

    while num > 0:
        counter[num % 3] += 1
        num //= 3
    
    return counter[1] > counter[2]

def Delete(head):
    curr=Node()
    curr.next = head
    while curr.next is not None:
        currVal=curr.next.val
        if CntIn3(currVal):
            curr.next=curr.next.next
        else:
            curr=curr.next
