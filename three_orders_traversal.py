class Node(object):

    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self,value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self,left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

# Use recursion and perform pre-order traversal
# def pre_order(tree):
#     cur_node = tree.get_root()

#     visit_order = []

#     visit_order.append(cur_node.value)

#     def traverse(node):
#         if node is None:
#             return

#         if node.has_left_child():
#             cur = node.get_left_child()
#             visit_order.append(cur.value)
#             traverse(cur)

#         if node.has_right_child():
#             cur = node.get_right_child()
#             visit_order.append(cur.value)
#             traverse(cur)

#     traverse(cur_node)

#     return visit_order

def pre_order(tree):
    root = tree.get_root()

    visit_order = []

    def traverse(node):
        if node:
            # visit node
            visit_order.append(node.value)
            # traverse left
            traverse(node.get_left_child())
            # traverse right
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


# define in-order traversal
def in_order(tree):
    visit_order = []

    root = tree.get_root()

    def traverse(node):
        if node:
            # visit left node
            traverse(node.get_left_child())

            # visit node
            visit_order.append(node.value)

            # visit right node
            traverse(node.get_right_child())

    traverse(root)

    return visit_order


# define post_order traversal
def post_order(tree):
    visit_order = []

    root = tree.get_root()

    def traverse(node):
        if node:
            traverse(node.get_left_child())

            traverse(node.get_right_child())

            visit_order.append(node.value)

    traverse(root)

    return visit_order


tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

pre_order(tree)
in_order(tree)
post_order(tree)
