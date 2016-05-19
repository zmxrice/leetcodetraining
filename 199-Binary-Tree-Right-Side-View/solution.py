# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        level = [root]
        res = []
        while level:
            next = []
            res.append(level[-1].val)
            for i in level:
                if i.left:
                    next.append(i.left)
                if i.right:
                    next.append(i.right)
            level = next
        return res
            