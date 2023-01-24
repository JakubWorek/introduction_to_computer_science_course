#Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
#się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
#drugiej elementy występują w przypadkowej kolejności. Proszę napisać
#funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
#elementy będą stanowić sumę mnogościową elementów z list wejściowych.
#Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
#zwrócić wskazanie na listę wynikową. Na przykład dla list:
#2 -> 3 -> 5 ->7-> 11
#8 -> 2 -> 7 -> 4
#powinna pozostać lista:
#2 -> 3 -> 4 -> 5 ->7-> 8 -> 11

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def inList(lst, val):
    if lst.val == None:
        lst = lst.next
    
    while lst != None and lst.val < val:
        lst = lst.next

    return lst != None and lst.val == val

#l1 - posortowana, l2 - nieposortowana
def sum(l1, l2):
    curr1 = Node()
    curr1.next=l1
    curr2 = Node()
    curr2.next=l2

    while curr2.next is not None:
        if not inList(curr1, curr2.next.val):
            tmp1=curr1
            while tmp1.next != None and tmp1.next.val < curr2.next.val:
                tmp1 = tmp1.next
            
            if tmp1.next == None:
                tmp1.next = Node(curr2.next.val)
                return
            
            if tmp1.next.val == curr2.next.val:
                return
            
            new = Node(curr2.next.val)
            new.next = tmp1.next
            tmp1.next = new
        
        curr2=curr2.next
    
    return l1