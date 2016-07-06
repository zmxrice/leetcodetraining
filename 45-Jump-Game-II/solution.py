class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        curMax, i, res = 0, 0, 0
        while curMax < len(nums)-1:
            lastMax = curMax
            while i <= lastMax:
                curMax = max(curMax, i+nums[i])
                i += 1
            res += 1
        return res