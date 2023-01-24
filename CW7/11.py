#Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
#której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
#element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
#elementu o zadanym kluczu brak w liście należy element o takim kluczu
#wstawić do listy.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def addOrDelete(head, key):
    guard=Node()
    guard.next = head

    curr=guard
    while curr.next is not None:
        if curr.next.val == key:
            curr.next = curr.next.next
            return True
        curr = curr.next

    curr.next = Node(key)
    return False

