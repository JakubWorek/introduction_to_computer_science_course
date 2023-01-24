#Elementy w liście są uporządkowane według wartości klucza. Proszę
#napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do
#funkcji przekazujemy wskazanie na pierwszy element listy,
#funkcja powinna zwrócić liczbę usuniętych elementów.

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def remove_none_unique(head):
    current = head
    while current.next is not None and\
         current.next.next is not None:
        if current.next.val == current.next.next.val:
            temp = current.next.next
            while temp is not None and temp.val == temp.next.val:
                temp=temp.next
            current.next=temp
        else:
            current=current.next