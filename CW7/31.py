# 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
# powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
# wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
# powinna zwrócić liczbę usuniętych elementów. 

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# p - lista ktora chcemy rozdzielic, nie ma wartownika
# a - lista z parzystymi dodatnimi
# b - lista ta druga
def rozdziel(p, a, b):
    cnt = 0
    # dorabiamy wartownik

    p = Node(None, p)

    while p.next != None:
        q = p.next

        p.next = p.next.next

        if q.val % 2 == 0 and q.val > 0:
            q.next = a.next
            a.next = q
        elif q.val % 2 == 1 and q.val < 0:
            q.next = b.next
            b.next = q
        else:
            cnt += 1

    return cnt
    