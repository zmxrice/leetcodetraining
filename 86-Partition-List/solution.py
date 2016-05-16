# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less, more = ListNode(0), ListNode(0)
        curL, curM = less, more
        while head:
            if head.val < x:
                curL.next = head
                curL, head = curL.next, head.next
            else:
                curM.next = head
                curM, head = curM.next, head.next
        curL.next = more.next
        curM.next = None
        return less.next