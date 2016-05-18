# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        level = [root]
        res = []
        while level:
            next = []
            for node in level:
                if node:
                    res.append(node.val)
                    if node.left:
                        next.append(node.left)
                    else:
                        next.append(None)
                    if node.right:
                        next.append(node.right)
                    else:
                        next.append(None)
                else:
                    res.append(None)
            level = next
        while res[-1] == None:
            res.pop()
        return str(res)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = eval(data)
        if not data:
            return None
        tag = False
        root = TreeNode(data[0])
        cur = deque()
        cur.append(root)
        for i in data[1:]:
            if not tag:
                if i != None:
                    left = TreeNode(i)
                    cur.append(left)
                    cur[0].left = left
                tag = True
                continue
            if i != None:
                right = TreeNode(i)
                cur.append(right)
                cur[0].right = right
            tag = False
            cur.popleft()
        return root
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))