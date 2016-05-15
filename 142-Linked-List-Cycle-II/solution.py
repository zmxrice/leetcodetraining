# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            fast, slow = head, head
            while True:
                fast, slow = fast.next.next, slow.next
                if fast is slow:
                    break
            cur = head
            while True:
                if cur is slow:
                    return cur
                cur, slow = cur.next, slow.next
        except:
            return None