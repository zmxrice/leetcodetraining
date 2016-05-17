# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre, cur = None, head
        for i in xrange(2):
            cur.next, pre, cur = pre, cur, cur.next
        head.next = self.swapPairs(cur)
        return pre