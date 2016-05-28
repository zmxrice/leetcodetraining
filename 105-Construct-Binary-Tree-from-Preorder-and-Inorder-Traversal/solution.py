# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, preorder, a, b, inorder, c, d):
        if a > b:
            return
        root = TreeNode(preorder[a])
        i = inorder.index(root.val)
        root.left = self.helper(preorder, a+1, a+i-c, inorder, c, i-1)
        root.right = self.helper(preorder, a+i-c+1, b, inorder, i+1, d)
        return root
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)