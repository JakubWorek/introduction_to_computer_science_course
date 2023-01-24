# Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza” od pierwszej litery s2. Według
# tej zasady rozmieszczono napisy w liście cyklicznej, na przykład:
# ┌─bartek──leszek──marek──ola──zosia─┐
# └───────────────────────────────┘
# Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy napis z zachowaniem
# zasady poprzedzania. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, funkcja
# powinna zwrócić wartość logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
# elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def insert(cycle, val):
    if cycle.val == None:
        cycle = cycle.next

    head = cycle

    while True:
        curr = cycle
        while curr.next != cycle:
            if ord(val[-1]) > ord(curr.next.val[0])\
                or ord(curr.val[-1]) > ord(val[0]):
                break
            curr=curr.next
        else:
            q=Node(val)
            q.next=cycle.next
            cycle.next = q
            return True

        cycle = cycle.next
        if cycle == head: 
            return False