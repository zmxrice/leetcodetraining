# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        oddHead = odd = head
        evenHead = even = head.next
        cur = even.next
        isOdd = True
        while cur:
            if isOdd:
                odd.next = cur
                odd = odd.next
                isOdd = False
            else:
                even.next = cur
                even = even.next
                isOdd = True
            cur = cur.next
        odd.next = evenHead
        even.next = None
        return oddHead