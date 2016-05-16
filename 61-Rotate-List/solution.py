# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        count, cur = 0, head
        while cur:
            count += 1
            cur = cur.next
        k %= count
        if k == 0:
            return head
        slow = fast = head
        for i in xrange(k):
            fast = fast.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next
        trueHead = slow.next
        slow.next = None
        fast.next = head
        return trueHead