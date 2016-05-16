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
        slow, fast = head, head.next
        while fast:
            if not fast.val == slow.val:
                slow.next = fast
                slow = slow.next
            fast = fast.next
        slow.next = None
        return head