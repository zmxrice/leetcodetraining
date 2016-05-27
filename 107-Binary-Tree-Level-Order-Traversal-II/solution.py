# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level = [root]
        res = []
        while level:
            next, curVals = [], []
            for node in level:
                curVals.append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)
            level = next
            res.append(curVals)
        return res[::-1]