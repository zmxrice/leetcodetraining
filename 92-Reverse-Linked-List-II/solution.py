# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start, cur = None, head
        for i in xrange(m-1):
            start = cur
            cur = cur.next
        end = None
        for i in xrange(n-m+1):
            cur = cur.next
            end = cur
        pre, cur = end, head
        if start:
            cur = start.next
        while cur is not end:
            cur.next, pre, cur = pre, cur, cur.next
        if start:
            start.next = pre
            return head
        else:
            return pre
            
        