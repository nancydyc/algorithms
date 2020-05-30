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
        1. traverse the tree by level
        2. find the highest leave node
        3. search the level after next level for leave node
        4. if there's a node at that level, return False => nodes at the same level has children and one of these children nodes also has child
        5. if there's no node at that level, return True => nodes at the same level has no children nodes or their children nodes has no children

    """

    q = []
    q.append(tree)

    while q:
        cur_node = q.pop()
        # print(f'check {cur_node.value}')
        if cur_node.left:
            q.append(cur_node.left)

        if cur_node.right:
            q.append(cur_node.right)

        if q and not cur_node.left and not cur_node.right:
            # print(f'q has {[i.value for i in q]}')
            if q[-1].left or q[-1].right:
                if q[-1].left.left or q[-1].left.right or q[-1].right.left or q[-1].right.right:
                    return False

    return True


a = BinaryTreeNode('1')
b = a.insert_left('2')
c = a.insert_right('3')
# a--c: return True
d = b.insert_left('4')
e = b.insert_right('5')
f = d.insert_left('6')
# a--f: return False






