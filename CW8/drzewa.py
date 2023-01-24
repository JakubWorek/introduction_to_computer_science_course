class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def wypisz(p):
    if p != None:
        wypisz(p.left)
        print(p.val)
        wypisz(p.right)

def czyZawiera(p, key):
    if p != None:
        if p.val == key:
            return True
        
        return czyZawiera(p.left, key) or\
            czyZawiera(p.right, key)
    return False

def rozmiar(p):
    if p != None:
        return 1+rozmiar(p.left)+rozmiar(p.right)
    return 0

def wysokosc(p,lvl):
    if p is None: return lvl
    else:
        return max(wysokosc(p.left,lvl+1),\
            wysokosc(p.right,lvl+1))

def count_leaves(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    return count_leaves(root.left)\
        + count_leaves(root.right)

def count_nodes_at_level(root, n):
    if not root:
        return 0
    if n == 1:
        return 1
    return count_nodes_at_level(root.left, n-1)\
            + count_nodes_at_level(root.right, n-1)

def count_single_child_nodes(root):
    if not root:
        return 0
    count = 0
    if (root.left and not root.right) or\
        (not root.left and root.right):
        count += 1
    count += count_single_child_nodes(root.left)
    count += count_single_child_nodes(root.right)
    return count

def delete_tree(root):
    if not root:
        return 
    delete_tree(root.left)
    delete_tree(root.right)
    del root

def delete_nodes_above_level(root, level, current_level=1):
    if not root:
        return
    if current_level > level:
        delete_nodes_above_level(root.left, level, current_level+1)
        delete_nodes_above_level(root.right, level, current_level+1)
        del root
        return None
    root.left = delete_nodes_above_level(root.left, level, current_level+1)
    root.right = delete_nodes_above_level(root.right, level, current_level+1)
    return root

def is_in_bst(root, val):
    if not root:
        return False
    if root.val == val:
        return True
    if val < root.val:
        return is_in_bst(root.left, val)
    else:
        return is_in_bst(root.right, val)

def insert_in_BST(root, x):
    if not root:
        return Node(x)
    if x < root.val:
        root.left = insert_in_BST(root.left, x)
    else:
        root.right = insert_in_BST(root.right, x)
    return root

def is_bst(root, left=None, right=None):
    if not root:
        return True
    if left and root.val <= left.val:
        return False
    if right and root.val >= right.val:
        return False
    return is_bst(root.left, left, root) and is_bst(root.right, root, right)

def is_bst_avl(root):
    if not root:
        return True
    left_height = wysokosc(root.left, 0)
    right_height = wysokosc(root.right, 0)
    if abs(left_height - right_height) > 1:
        return False
    return is_bst_avl(root.left) and is_bst_avl(root.right)

def array_to_bst(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = array_to_bst(arr[:mid])
    root.right = array_to_bst(arr[mid+1:])
    return root


def main():
    root=array_to_bst([1,2,3,4,5,6,7,8,9])
    print(is_bst(root))

if __name__ == '__main__': main()