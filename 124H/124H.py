# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxPathSum(self, root) -> int:
        self.res = root.val

        def dfs(node):  # if node is the end of the the path
            if not node:
                return 0
            l = dfs(node.left) + node.val if dfs(node.left) > 0 else node.val
            r = dfs(node.right) + node.val if dfs(node.right) > 0 else node.val
            # through the node
            self.res = max(self.res, l + r - node.val)
            return max(l, r)

        dfs(root)
        return self.res

    def passRoot(self, root):
        def max_gain(root):
            if not root:
                return 0
            left_gain = max(max_gain(root.left), 0)
            right_gain = max(max_gain(root.right), 0)
            return root.val + max(left_gain, right_gain)

        left = max_gain(root.left)  # at least 0
        right = max_gain(root.right)  # at least 0
        max_sum = root.val + left + right
        return max_sum

