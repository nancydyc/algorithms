"""
Given a sorted(increasing order) array with unique interger
element, write an algorithm to create a binary search tree
with minimal height.
"""

class Node():
    """
         Solution:
         1. when the tree is balanced, the height is min
         2. left most child node is the smallest interger, right most is the largest.

        For example:
        [1, 2, 3, 4, 5, 6, 7]
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def min_bst(arr): # recursive solution
    if arr == []:
        return None

    else:
        mid = len(arr) // 2
        tree = Node(arr[mid])

        tree.left = min_bst(arr[:mid])

        tree.right = min_bst(arr[mid:])

        return tree




