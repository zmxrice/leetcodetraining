# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, inorder, a,b, postorder, c, d):
        if a > b or c > d:
            return
        root = TreeNode(postorder[d])
        i = inorder.index(root.val)
        root.left = self.helper(inorder, a, i-1, postorder, c, c+i-a-1)
        root.right = self.helper(inorder, i+1, b, postorder, c+i-a, d-1)
        return root
        
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        