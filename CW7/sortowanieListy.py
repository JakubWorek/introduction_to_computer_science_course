class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def sort(head):
    # if 0,1 or 2 nodes:
    if head is None: return None
    elif head.next is None: return head
    elif head.next.next is None:
        if head.next.val < head.val:
            helper = head.next
            head.next = None
            helper.next = head
            head = helper
            return head
        else: return head
    #function to sort (min 3 nodes):
    flag = True
    while flag:
        flag = False
        if head.val > head.next.val:
            flag = True
            helper = head.next
            head.next = head.next.next
            helper.next = head
            head = helper

        node1=head
        node2=node1.next

        while node2.next is not None:
            if node2.next.val < node2.val:
                flag = True
                helper = node2.next
                node2.next = node2.next.next
                node1.next = helper
                helper.next = node2
            node1 = node2
            node2=node2.next

    return head
