#1. Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
#struktury listy odsyłaczowej.
#- czy element należy do zbioru
#- wstawienie elementu do zbioru
#- usunięcie elementu ze zbioru

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class Set:
    def __init__(self):
        self.head = None


    def contains(self, val):
        current = self.head
        while current is not None:
            if current.val == val:  
                return True
            current = current.next
        return False


    def add(self, val):
        if not self.contains(val):
            newNode=Node(val)
            if self.head is None:
                self.head = newNode
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = newNode


    def remove(self, val):
        current = self.head
        if (current is not None):
            if (current.val == val):
                self.head = current.next
                current = None
                return

        while (current is not None):
            if current.val == val:
                break
            prev = current
            current = current.next
        if (current == None):
            return

        prev.next = current.next
        current = None


    def print(self):
        curr=self.head
        while curr != None:
            print(curr.val)
            curr=curr.next


def main():
    mySet = Set()
    mySet.add(7)
    mySet.add(5)
    mySet.add(3)
    mySet.add(3)
    mySet.print()
    print("--------------------------------")
    mySet.remove(7)
    mySet.print()

if __name__ == '__main__': main()