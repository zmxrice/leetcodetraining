# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMax(self, root):
        if not root:
            return 0,0
        leftMax, noLeft = self.getMax(root.left)
        rightMax, noRight = self.getMax(root.right)
        return max(leftMax+rightMax, root.val+noLeft+noRight), leftMax+rightMax
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.getMax(root)[0]