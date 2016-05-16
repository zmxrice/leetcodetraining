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
        res, s = [], set()
        cur = head
        while cur:
            if cur.val not in s:
                res.append(cur)
                s.add(cur.val)
            elif res and res[-1].val == cur.val:
                res.pop()
            cur = cur.next
        if not res:
            return None
        head = res[0]
        for i in xrange(len(res)-1):
            res[i].next = res[i+1]
        res[-1].next = None
        return head