# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                cur, l1 = cur.next, l1.next
            else:
                cur.next = l2
                cur, l2 = cur.next, l2.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next