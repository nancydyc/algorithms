class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def validate_bst(tree):
    """ Given a binary tree, check if it is a binary search tree.

          y 5
           / \
         x 3 z 6

           a 4
            / \
         b 3  c 6
              / \
           d 1  e 10

        - do an inorder traversal of the binary tree
        - if any right node is smaller than left node
        - return False
        - else return True when finishing traversal

    runtime: O(n) + O(n) -> O(n)
    space: O(n)
    n is the number of nodes in the tree

    """


    visit_order = []

    def traverse(node):
        if not node:
            return

        traverse(node.left)

        visit_order.append(node.value)

        traverse(node.right)

    traverse(tree)

    for i in range(1, len(visit_order)):
        if visit_order[i] < visit_order[i - 1]:
            return False

    return True

# Tree 1 --> True
Y = BinaryTreeNode(5)
X = Y.insert_left(3)
Z = Y.insert_right(6)

# Tree 2 --> False
A = BinaryTreeNode(4)
B = A.insert_left(3)
C = A.insert_right(6)
D = C.insert_left(1)
E = C.insert_right(10)



