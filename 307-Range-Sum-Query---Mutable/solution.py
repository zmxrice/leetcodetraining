class SegTreeNode(object):
    def __init__(self, start, end):
        self.val = 0
        self.start = start
        self.end = end
        self.left = None
        self.right = None

class NumArray(object):
    def buildTree(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            root = SegTreeNode(start, end)
            root.val = nums[start]
            return root
        root = SegTreeNode(start, end)
        mid = (start+end) / 2
        root.start = start
        root.end = end
        root.left = self.buildTree(nums, start, mid)
        root.right = self.buildTree(nums, mid+1, end)
        root.val = root.left.val+root.right.val
        return root

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.root = self.buildTree(nums, 0, len(nums)-1)
        self.nums = nums


    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        cur = self.root
        diff = val - self.nums[i]
        self.nums[i] = val
        while cur:
            cur.val += diff
            if cur.left and cur.left.start <= i <= cur.left.end:
                cur = cur.left
            elif cur.right and cur.right.start <= i <= cur.right.end:
                cur = cur.right
            else:
                break

    def getVal(self, cur, i, j):
        if cur.start == i and cur.end == j:
            return cur.val
        if j <= cur.left.end:
            return self.getVal(cur.left, i, j)
        if i >= cur.right.start:
            return self.getVal(cur.right, i, j)
        return self.getVal(cur.left, i, cur.left.end) + self.getVal(cur.right, cur.right.start, j)

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        cur = self.root
        return self.getVal(cur, i, j)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)