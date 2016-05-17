# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n == 0:
            return head
        fast, slow = head, head
        for i in xrange(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast and fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head