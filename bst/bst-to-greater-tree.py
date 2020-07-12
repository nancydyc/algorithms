# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    total = 0

    def convertBST(self, root):
        """
        Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST
        is changed to the original key plus sum of all keys greater than the original key in BST.

        Input: The root of a Binary Search Tree like this:
                  5
                /   \
               2     13

        Output: The root of a Greater Tree like this:
                 18
                /   \
              20     13
        """

        if root:

            self.convertBST(root.right)

            self.total += root.val

            root.val = self.total

            self.convertBST(root.left)

        return root

# Alternative solution: Iterative solution using Stack
def convert_bst(root):
    total = 0
    node = root
    s = []
    while s or node:
        # move to the rightmost node
        while node:
            s.append(node)
            node = node.right

        cur_node = s.pop()
        # track the total value
        total += cur_node.val
        # convert the value
        cur_node.val = total
        # check if a left node exists;
        # if stack becomes empty and no more left node in the tree, stop the loop
        node = cur_node.left

    return root


b = TreeNode(2)
c = TreeNode(13)
a = TreeNode(5, b, c)

res = Solution()
res.convertBST(a)
print(a.val, b.val, c.val)

