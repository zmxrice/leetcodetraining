# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        pre, node1, node2, node3, node4 = None, None, None, None, None
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if pre:
                    if pre.val > root.val:
                        if not node1:
                            node1 = pre
                            node2 = root
                        else:
                            node3 = pre
                            node4 = root
                pre = root
                root = root.right
        if node1 and node4:
            node1.val, node4.val = node4.val, node1.val
        else:
            node1.val, node2.val = node2.val, node1.val