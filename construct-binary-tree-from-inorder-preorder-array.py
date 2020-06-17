class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

           3      3, [9,20,15,7]  left: 9     right: 15, 20, 7
          / \


              3   9, [20,15,7]  left: /    right: 15,20,7
             / \
            9

          3       20, [15,7]  left: 15  right: 7
         / \
        9   20
            / \

      3
     / \           15, [7] left: /  right: 7
    9   20
        / \        7, []  left: / right: /
       15  7

    """
    # Solution: recursive
    # each node is a tree itself, recursively find the root and the root for left and right subtree
    # if (left or right) inorder arr is empty, done, return root node

    def helper(left=0, right=len(inorder)):
        nonlocal preorder_index

        if left == right:
            return None

        root_val = preorder[preorder_index]
        root = TreeNode(root_val)
        # print(f'------ Check Node {root.val}')

        index = idx_dict[root_val]
        # print(f'point to inorder arr index {index}')

        preorder_index += 1

        # print(left, index)
        root.left = helper(left, index)

        # print(index + 1, right)
        root.right = helper(index + 1, right)

        return root

    preorder_index = 0

    idx_dict = {value:index for index, value in enumerate(inorder)}

    return helper()

result = buildTree([3,9,20,15,7], [9,3,15,20,7])


def print_tree(node):
    """ Give the root node, print the whole tree. """

    path = str(node.val)
    q = [(node, path)]

    while q:
        level_size = len(q)
        for i in range(level_size):
            cur = q.pop(0)[0]
            if i == 0:
                path += '\n'

            if cur is None:
                continue

            if cur.left:
                path += str(cur.left.val) + '|'
                q.append((cur.left, path))

            else:
                path += 'Null|'
                q.append((None, path))

            if cur.right:
                path += str(cur.right.val) + '|'
                q.append((cur.right, path))

            else:
                path += 'Null|'
                q.append((None, path))

        path = path[:-1]

    return path

print(print_tree(result))
