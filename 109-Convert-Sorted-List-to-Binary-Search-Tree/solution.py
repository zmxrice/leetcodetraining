# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convert(self, head, count):
        if count == 0:
            return None
        if count == 1:
            return TreeNode(head.val)
        half = count/2
        cur = head
        for i in xrange(half):
            cur = cur.next
        root = TreeNode(cur.val)
        root.left = self.convert(head, half)
        root.right = self.convert(cur.next, count-half-1)
        return root
        
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        count, cur = 0, head
        while cur:
            count += 1
            cur = cur.next
        return self.convert(head, count)