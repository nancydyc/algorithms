"""
Write an algo to find the "next" node of a given node in a bst. In order traversal. Assume each node has a link to its parent.

                 5
               /   \
             2       6
           /   \
          1     4
               / \
              3  4.5
5 [1, 2, 4]

given root = 5
depth first search with left preference
- recursive solution

visited = [] // empty list that holds nodes already visited
    - current = root
    base case: (if current.left is None):
    - return None
    flow control
    - current = current.left
    if visited[-1].data is node.data:
      return current node
    - visited.append(current node)
    - current = current.right

return visited

Call stack:
5 r l
2 r l
1 None None

runtime: O(n)
space: O(n) n is the number of the nodes

- find the node in the tree
- return the next node

Input: tree, node
Output: next node

"""

class Node():
    """Node class"""

    def __init__(self, data, left = None, right = None, parent = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"<node| data: {self.data}, left: {self.left}, right: {self.right}>"

def inorder(tree, node, visited = []):
    """in order traversal of a tree given the root node"""

    if tree is None:
        return

    inorder(tree.left, node, visited)

    if visited and node.data == visited[-1].data:
      return tree.data

    visited.append(tree)
    inorder(tree.right, node, visited)

    return visited


six = Node(6)
one = Node(1)
four = Node(4)
two = Node(2, one, four)
root = Node(5, two, six)
