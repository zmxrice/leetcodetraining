# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = dummy = ListNode(0)
        tag = False
        fast, slow = head.next, head
        while fast:
            if fast.val == slow.val:
                tag = True
            elif tag:
                tag = False
            else:
                cur.next = slow
                cur = cur.next
            fast, slow = fast.next, slow.next
        if tag:
            cur.next = None
        else:
            cur.next = slow
        return dummy.next