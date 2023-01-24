# Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
#liście ułożone są według rosnących potęg. Proszę napisać funkcję
#obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
#są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
#utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
#powinny pozostać niezmienione.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def subtract(w1, w2):
    ans = Node()
    c = ans

    if w1.val == None:
        w1 = w1.next
    if w2.val == None:
        w2 = w2.next


    while w1 != None or w2 != None:
        v = 0
        if w1 != None:
            v += w1.val
            w1 = w1.next
        if w2 != None:
            v -= w2.val
            w2 = w2.next
        
        c.next = Node(v)
        c = c.next

    return ans