# def right_total_value(node):
    # total = 0
    # nodes = [root]
    # # print(nodes)
    # while nodes:
    #     cur = nodes.pop()
    #     # print(cur.val)

    #     if cur != node and cur.val > node.val:
    #         # print(total)
    #         # return total + cur.val
    #         total += cur.val

    #     if cur.right and cur.right.val > node.val:
    #         nodes.append(cur.right)

    #     if cur.left and cur.left.val > node.val:
    #         nodes.append(cur.left)

    # return total + node.val

# current_total = right_total_value(root)
# print('root\'s new value', current_total)


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

b = TreeNode(2)
c = TreeNode(13)
a = TreeNode(5, b, c)

res = Solution()
res.convertBST(a)
print(a.val, b.val, c.val)

