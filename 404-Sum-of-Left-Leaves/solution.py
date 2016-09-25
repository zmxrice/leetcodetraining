# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        res = 0
        level = [root]
        while level:
            nex = []
            for node in level:
                if node.left:
                    if not node.left.left and not node.left.right:
                        res += node.left.val
                    else:
                        nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            level = nex
        return res