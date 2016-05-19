# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leftHeight(self, root):
        if not root:
            return 0
        height = 0
        while root:
            height += 1
            root = root.left
        return height
    
    def rightHeight(self, root):
        if not root:
            return 0
        height = 0
        while root:
            height += 1
            root = root.right
        return height
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.leftHeight(root.left)
        right = self.rightHeight(root.right)
        if left == right:
            return 2**(left+1)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
            
        