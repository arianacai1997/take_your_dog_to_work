# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # my solution
    def findTilt(self, root) -> int:
        def total(node):
            if not node:
                return 0
            return node.val + total(node.right) + total(node.left)

        self.res = 0

        def traverse(node):
            if not node:
                return 0
            traverse(node.left)
            traverse(node.right)
            self.res += abs(total(node.left) - total(node.right))

        traverse(root)
        return self.res

    def findTilt2(self, root):
        def tilt(root):
            # return (sum, tilt) of tree
            if not root: return (0, 0)
            left = tilt(root.left)
            right = tilt(root.right)
            return (left[0] + right[0] + root.val, abs(left[0] - right[0]) + left[1] + right[1])

        return tilt(root)[1]

"""Think about a recursive function. Beside the tilt of subtrees, we also need to get the sum of subtrees.
So I came up with the idea of sub function tilt(root), which returns the tuple (sum, tilt) of tree"""