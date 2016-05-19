# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                if k > 1:
                    root = stack.pop()
                    root = root.right
                    k -= 1
                else:
                    return stack.pop().val