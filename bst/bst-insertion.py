from collections import deque

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


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self,value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


class Tree():
    def __init__(self):
        self.root = None

    def set_root(self,value):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def compare(self,node, new_node):
        """
        0 means new_node equals node
        -1 means new node less than existing node
        1 means new node greater than existing node
        """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1

    """
    define insert here
    can use a loop (try one or both ways)
    """
    def insert_with_loop(self,new_value):
        node = self.get_root()
        new_node = Node(new_value)

        if node is None:
            self.root = new_node
            return

        while True:
#             print(f'Next compare {node} with new value {new_node}')

            num = self.compare(node, new_node)

            if num == 0:
                node.set_value(new_node)
#                 print(f'set node {node} value {new_node.value}')
                break

            elif num == 1:
                if node.has_right_child():
                    node = node.get_right_child()
#                     node = Node(node)

                else:
                    node.set_right_child(new_node)
#                     print(f'set node {node.right} value {new_node.value}')
                    break

            else:
                if node.has_left_child():
                    node = node.get_left_child()
#                     node = Node(node)

                else:
                    node.set_left_child(new_node)
#                     print(f'set node {node.left} value {new_node.value}')
                    break
#         print('----------------------------------------------')


    """
    define insert here (can use recursion)
    try one or both ways
    """
    def insert_recursively(self, new_node, node):
        num = self.compare(node, new_node)
        if num == 0:
            node.set_value(new_node.value)
            return

        elif num == 1:
            if not node.right:
                return node.set_right_child(new_node)
            else:
                self.insert_recursively(new_node, node.right)

        else:
            if not node.left:
                return node.set_left_child(new_node)
            else:
                self.insert_recursively(new_node, node.left)

    def insert_with_recursion(self,value):
        # compare (use above helper function)
        # if value is greater than current node, check if right has child
        # if value is less than current node, check if left has child
        # when no child or equal, set the value and return

        node = self.get_root()
        new_node = Node(value)

        if not node:
            self.root = new_node
            return

        self.insert_recursively(new_node, node)



    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level


        return s


tree = Tree()
tree.insert_with_loop(5)
tree.insert_with_loop(6)
tree.insert_with_loop(4)
tree.insert_with_loop(2)
tree.insert_with_loop(5) # insert duplicate
print(tree)

# Tree

# Node(Node(5))
# Node(4) | Node(6)
# Node(2) | <empty> | <empty> | <empty>
# <empty> | <empty>

tree = Tree()
tree.insert_with_recursion(5)
tree.insert_with_recursion(6)
tree.insert_with_recursion(4)
tree.insert_with_recursion(2)
tree.insert_with_recursion(5) # insert duplicate
print(tree)

# Tree

# Node(Node(5))
# Node(4) | Node(6)
# Node(2) | <empty> | <empty> | <empty>
# <empty> | <empty>
