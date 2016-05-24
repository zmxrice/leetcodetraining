# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, sum, res, path, curSum):
        if not root.left and not root.right:
            if curSum+root.val == sum:
                res.append(path+[root.val])
            return
        if root.left:
            self.helper(root.left, sum, res, path+[root.val], curSum+root.val)
        if root.right:
            self.helper(root.right, sum, res, path+[root.val], curSum+root.val)
            
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        self.helper(root, sum, res, [], 0)
        return res