# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeSort(self, head, count):
        if not head or not head.next:
            return head
        half = count / 2
        leftHead = head
        for i in xrange(half-1):
            head = head.next
        rightHead = head.next
        head.next = None
        left = self.mergeSort(leftHead, half)
        right = self.mergeSort(rightHead, count-half)
        res = ListNode(0)
        cur = res
        while left and right:
            if left.val < right.val:
                cur.next = left
                cur, left = cur.next, left.next
            else:
                cur.next = right
                cur, right = cur.next, right.next
        if left:
            cur.next = left
        if right:
            cur.next = right
        return res.next
        
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        return self.mergeSort(head, count)