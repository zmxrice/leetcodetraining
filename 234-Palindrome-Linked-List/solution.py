# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        fast, slow = head, head
        try:
            while True:
                fast = fast.next.next
                slow = slow.next
        except:
            pre = None
            cur = slow
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            while pre and head:
                if head.val != pre.val:
                    return False
                pre, head = pre.next, head.next
            return True