# Definition for a binary tree node.
"""
A preorder traversal is:

(root node) (preorder of left branch) (preorder of right branch)
While a postorder traversal is:

(postorder of left branch) (postorder of right branch) (root node)
For example, if the final binary tree is [1, 2, 3, 4, 5, 6, 7] (serialized), then the preorder traversal is [1] + [2, 4, 5] + [3, 6, 7], while the postorder traversal is [4, 5, 2] + [6, 7, 3] + [1].

If we knew how many nodes the left branch had, we could partition these arrays as such, and use recursion to generate each branch of the tree.

Algorithm

Let's say the left branch has LL nodes. We know the head node of that left branch is pre[1], but it also occurs last in the postorder representation of the left branch. So pre[1] = post[L-1] (because of uniqueness of the node values.) Hence, L = post.indexOf(pre[1]) + 1.

Now in our recursion step, the left branch is represnted by pre[1 : L+1] and post[0 : L], while the right branch is represented by pre[L+1 : N] and post[L : N-1].
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        L = post.index(pre[1]) + 1 # num of nodes in left tree and the head is pre[1]
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root

    # cache space
    def constructFromPrePost2(self, pre, post):
        def make(i0, i1, N):
            if N == 0:
                return None
            root = TreeNode(pre[i0])
            if N == 1:
                return root

            for L in range(N):
                if post[i1 + L - 1] == pre[i0 + 1]:
                    break

            root.left = make(i0 + 1, i1, L)
            root.right = make(i0 + L + 1, i1 + L, N - 1 - L)
            return root

        return make(0, 0, len(pre))
