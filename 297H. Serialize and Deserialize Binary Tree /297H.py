# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # level-order, iteration

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = ''
        if not root:
            return res
        level_pool = [root]
        res = str(root.val)
        while level_pool:
            child_pool = []
            for node in level_pool:
                if node.left:
                    res += ',' + str(node.left.val)
                    child_pool.append(node.left)
                else:
                    res += ',#'
                if node.right:
                    res += ',' + str(node.right.val)
                    child_pool.append(node.right)
                else:
                    res += ',#'
            level_pool = child_pool
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        ls = data.split(',')
        root = TreeNode(int(ls[0]))  # 可以pop
        node_pool = [root]
        idx = 1
        num_child = 2  # for root, only left & right
        while idx < len(ls):
            child_pool = []
            child_level = ls[idx: idx + num_child]
            for i, node in enumerate(node_pool):
                left = child_level[2 * i]
                right = child_level[2 * i + 1]
                if left != '#':
                    node.left = TreeNode(int(left))
                    child_pool.append(node.left)
                if right != '#':
                    node.right = TreeNode(int(right))
                    child_pool.append(node.right)
            node_pool = child_pool
            idx += num_child
            num_child = 2 * len(node_pool)
        return root


class Codec:
    # preorder, recursion

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        ls = data.split(',')

        def des(ls):
            val = ls.pop(0)
            if val == '#':  # cannot use "if ls[0] == '#'", it has to be popped!
                return None
            node = TreeNode(int(val))
            node.left = des(ls)  # popped once
            node.right = des(ls)  # ls is different from the above
            return node

        return des(ls)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))