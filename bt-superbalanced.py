"""
A tree is "superbalanced" if the difference between the depths
of any two leaf nodes is no greater than one.
"""
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

def check_superbalanced(tree):
    """
        1. traverse the tree
        2. if it has left child, check if it has right child
        3. if not, return False
    """
