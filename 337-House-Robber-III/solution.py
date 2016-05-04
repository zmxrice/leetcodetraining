# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if not root:
            return 0,0
        left, notLeft = self.helper(root.left)
        right, notRight = self.helper(root.right)
        #max_val, not including current node
        return max(left+right, root.val+notLeft+notRight), left+right
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root)[0]