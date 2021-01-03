# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        # pre, slow are the mid node
        # but we have to cut off the first half for the left tree
        # left: head-pre, root: slow, right: slow.next-the end
        pre.next = None
        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def find_size(head):
            ptr = head
            size = 0
            while ptr:
                ptr = ptr.next
                size += 1
            return size

        def formBST(l, r):
            nonlocal head
            if l > r:
                return None
            mid = (l + r) // 2
            left = formBST(l, mid - 1)
            node = TreeNode(head.val)
            node.left = left
            head = head.next
            node.right = formBST(mid + 1, r)
            return node

        size = find_size(head)
        return formBST(0, size - 1)

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def find_mid(start, end):
            slow = fast = start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            return slow

        def formBST(start, end):
            if start == end:
                return
            mid = find_mid(start, end)
            node = TreeNode(mid.val)
            node.left = formBST(start, mid)
            node.right = formBST(mid.next, end)
            return node

        return formBST(head, None)