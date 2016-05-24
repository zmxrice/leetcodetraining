# Definition for binary tree with next pointer.
# class TreeLinkNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution(object):
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return
        level = [root]
        while level:
            next = []
            for i in xrange(len(level)-1):
                level[i].next = level[i+1]
                
            for i in xrange(len(level)):
                if level[i].left:
                    next.append(level[i].left)
                if level[i].right:
                    next.append(level[i].right)
            level = next
            