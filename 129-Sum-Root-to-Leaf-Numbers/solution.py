# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import operator
class Solution(object):
    def getAllPaths(self, res, path, root):
        if not root.left and not root.right:
            res.append(path+str(root.val))
            return
        if root.left:
            self.getAllPaths(res, path+str(root.val), root.left)
        if root.right:
            self.getAllPaths(res, path+str(root.val), root.right)
        
        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = []
        self.getAllPaths(res, "", root)
        return reduce(operator.add, map(int, res))
        