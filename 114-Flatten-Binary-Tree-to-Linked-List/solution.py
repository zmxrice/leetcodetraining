# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        nodes = []
        stack = []
        while stack or root:
            if root:
                nodes.append(root)
                if root.right:
                    stack.append(root.right)
                root = root.left
            else:
                root = stack.pop()
        for i in xrange(len(nodes)-1):
            nodes[i].right = nodes[i+1]
            nodes[i].left = None