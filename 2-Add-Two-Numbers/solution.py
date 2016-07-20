# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = cur = ListNode(0)
        carry = 0
        while l1 and l2:
            cur.next = ListNode((l1.val+l2.val+carry)%10)
            carry = (l1.val+l2.val+carry)/10
            cur, l1, l2 = cur.next, l1.next, l2.next
            
        while l1:
            cur.next = ListNode((l1.val+carry)%10)
            carry = (l1.val+carry)/10
            cur, l1 = cur.next, l1.next
            
        while l2:
            cur.next = ListNode((l2.val+carry)%10)
            carry = (l2.val+carry)/10
            cur, l2 = cur.next, l2.next
            
        if carry:
            cur.next = ListNode(carry)
            
        return head.next