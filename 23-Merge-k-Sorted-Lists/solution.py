# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap, dummy = [], ListNode(0)
        cur = dummy
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        while heap:
            tmp = heapq.heappop(heap)[1]
            cur.next = tmp
            if tmp.next:
                heapq.heappush(heap,(tmp.next.val, tmp.next))
            cur = cur.next
        return dummy.next