# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        d = {}
        dummy = RandomListNode(0)
        cur1, cur2 = head, dummy
        while cur1:
            curNode = None
            if cur1.label in d:
                curNode = d[cur1.label]
            else:
                curNode = RandomListNode(cur1.label)
                d[cur1.label] = curNode
            if cur1.random:
                randomNode = None
                if cur1.random.label in d:
                    randomNode = d[cur1.random.label]
                else:
                    randomNode = RandomListNode(cur1.random.label)
                    d[cur1.random.label] = randomNode
                curNode.random = randomNode
            cur2.next = curNode
            cur1, cur2 = cur1.next, cur2.next
        return dummy.next
            