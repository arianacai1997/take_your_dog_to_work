# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        def recursion(curr):
            if not curr:
                return
            node = TreeNode(curr[0])
            if len(curr) == 1:
                return node
            flag = False
            for i in range(1, len(curr)):
                if curr[i] > curr[0]:
                    flag = True
                    break
            left = recursion(curr[1:]) if not flag else recursion(curr[1:i])
            right = recursion([]) if not flag else recursion(curr[i:])
            node.left = left
            node.right = right
            return node

        return recursion(preorder)
