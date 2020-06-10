class Node():
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right

class Tree():
    def __init__(self, root=None):
        self.root = root

class LL():
    def __init__(self):
        self.head = None
        self.tail = None

def create_lists_of_depths(tree):
    """
    Give a binary tree, design an algorithm which creates a linked list of all the nodes at each depth.

                     5
                  /     \
                3        7
               / \     /
              2   4   6

    [5]
    [3, 7]
    [2, 4, 6]

    1. traverse in level order
    2. for each level node, add them to linkedlist, add the head of ll to result list
    3. when finishing traversal, return the result list

    """


