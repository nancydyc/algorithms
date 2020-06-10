class Node():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

def create_lists_of_depths(node):
    """
    Give a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.

                     f:5
                   /     \
                 d:3      e:7
                /   \    /
              a:2  b:4  c:6

    [5]
    [3, 7]
    [2, 4, 6]

    1. traverse in level order
    2. for each level node, add them to linkedlist, add the head of ll to result list
    3. when finishing traversal, return the result list

    """

    q = []
    q.append(node)

    result = []

    while q:
        level_size = len(q)
        ll = LinkedList() # not sure if it will create an empty ll every time
        for i in range(len(q)):
            cur = q.pop(0)
            print('current node', cur.val)

            if ll.head is None:
                ll.head = cur
                ll.tail = cur
                result.append(ll.head)
                print(f'node{cur.val} level ll head is {ll.head.val}')

            else:
                ll.tail.next = cur
                ll.tail = cur
                print(f'node{cur.val} level ll head is {ll.head.val}, tail is now {ll.tail.val}')

            if cur.left:
                q.append(cur.left)

            if cur.right:
                q.append(cur.right)

        print('---------------------------')
    print(f'answer: linkedlists {[lhead.val for lhead in result]}')
    return result

a = Node(2)
b = Node(4)
c = Node(6)
d = Node(3, a, b)
e = Node(7, c)
f = Node(5, d, e)

# current node 5
# node5 level ll head is 5
# ---------------------------
# current node 3
# node3 level ll head is 3
# current node 7
# node7 level ll head is 3, tail is now 7
# ---------------------------
# current node 2
# node2 level ll head is 2
# current node 4
# node4 level ll head is 2, tail is now 4
# current node 6
# node6 level ll head is 2, tail is now 6
# ---------------------------
# answer: linkedlists [5, 3, 2]
# [<__main__.Node object at 0x7fdc008fe400>, <__main__.Node object at 0x7fdc008fe390>, <__main__.Node object at 0x7fdc01ef9a90>]




