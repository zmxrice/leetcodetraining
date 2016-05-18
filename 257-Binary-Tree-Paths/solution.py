# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def helper(self, res, path, root):
        if not root.left and not root.right:
            res.append(path+str(root.val))
        if root.left:
            self.helper(res, path+str(root.val)+"->", root.left)
        if root.right:
            self.helper(res, path+str(root.val)+"->", root.right)
        
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.helper(res, "", root)
        return res