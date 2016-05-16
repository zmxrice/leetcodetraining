# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def helper(self, head, k, count):
        if count < k:
            return head
        cur = head
        pre = None
        for i in xrange(k):
            cur.next, pre, cur = pre, cur, cur.next
        head.next = self.helper(cur, k, count-k)
        return pre
        
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        count, cur = 0, head
        while cur:
            count += 1
            cur = cur.next
        return self.helper(head, k, count)