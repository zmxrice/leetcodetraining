# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        count, cur = 0, head
        while cur:
            count += 1
            cur = cur.next
        half, cur = count / 2, head
        for i in xrange(half):
            cur = cur.next
        second = cur.next
        cur.next = None
        pre = None
        while second:
            second.next, pre, second = pre, second, second.next
        cur = head
        while cur and pre:
            tmp1, tmp2 = cur.next, pre.next
            cur.next = pre
            pre.next = tmp1
            cur = tmp1
            pre = tmp2