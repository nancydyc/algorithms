"""
Write an algo to find the "next" node of a given node in a bst.
In order traversal. Assume each node has a link to its parent.

                 5
               /   \
             2       6
           /   \
          1     4
               / \
              3  4.5


runtime: O(n)
space: O(n) n is the number of the nodes

Input: tree, node
Output: next node

-  if the node has a right node
    - return its leftmost child of the node's right subtree
-  if the node has no right node
    - check if it's a left child of its parent node
    - if true, return the parent node
    - else, make the parent node current node
        - compare with one-more-level-up parent node until meets the checking condition
        - if given node is the rightmost node, return none

"""

class Node():
    """ Node class, each node has a link to its parent node."""

    def __init__(self, data, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"<node| data: {self.data}, left: {self.left}, right: {self.right}>"


def leftmost_child(node):
    """ Get the left most child node of the right subtree."""
    if not node.left:
        return node

    res = leftmost_child(node.left)

    return res


def get_next_node(tree, node):
    if not node or not tree:
        return

    if node.right:
        return leftmost_child(node.right)

    cur = node
    p = cur.parent
    # print(p)
    while p and (p.left != cur):
        cur = node.parent
        p = cur.parent

    return p


six = Node(6)
one = Node(1)
four = Node(4)
two = Node(2, one, four)
root = Node(5, two, six)
six.parent = root
one.parent = two
four.parent = two
two.parent = root

print(get_next_node(root, six))
