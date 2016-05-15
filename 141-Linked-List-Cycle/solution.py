# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            fast, slow = head, head
            while True:
                fast, slow = fast.next.next, slow.next
                if fast is slow:
                    return True
        except:
            return False