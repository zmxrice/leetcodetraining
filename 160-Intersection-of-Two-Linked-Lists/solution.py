# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        countA, countB = 0, 0
        curA, curB = headA, headB
        while curA:
            countA += 1
            curA = curA.next
        while curB:
            countB += 1
            curB = curB.next
        if countA > countB:
            for i in xrange(countA-countB):
                headA = headA.next
        else:
            for i in xrange(countB-countA):
                headB = headB.next
        while headA:
            if headA is headB:
                return headA
            headA, headB = headA.next, headB.next
        return None
            
        