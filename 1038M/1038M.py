# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def post_order(node):
            if not node:
                return 0
            post_order(node.right)
            self.sum += node.val
            node.val = self.sum
            post_order(node.left)

        post_order(root)
        return root


