#2. Zastosowanie listy odsyłaczowej do implementacji
#tablicy rzadkiej. Proszę napisać trzy funkcje:
#– inicjalizującą tablicę,
#– zwracającą wartość elementu o indeksie n,
#– podstawiającą wartość value pod indeks n.

class Node:
    def __init__(self, val=None, ind=None):
        self.val = val
        self.ind = ind
        self.next = None


class Rzadka:
    def __init__(self):
        self.head = None


    def wartosc(self, i):
        current = self.head
        while current is not None and current.ind<i:
            current = current.next

        if current==None or current.i != i:
            return None

        return current.val


    def podstaw(self, val, n):
        if self.head is None:
            self.head = Node(val,n)
            return

        curr=self.head
        while curr.next != None and curr.next.ind < n:
            curr = curr.next
        
        if curr.next != None and curr.next.ind == n:
            curr.next.val = val
            return

        NewNode = Node(val,n)

        if curr.next == None: curr.next=NewNode
        else:
            NewNode.next=curr.next
            curr.next=NewNode


    def print(self):
        curr=self.head
        while curr != None:
            print(curr.val, curr.ind)
            curr=curr.next


def main():
    tab=Rzadka()
    tab.podstaw(123,14)
    tab.podstaw(68,5832)
    tab.podstaw(12,1)
    tab.print()


if __name__ == "__main__": main()