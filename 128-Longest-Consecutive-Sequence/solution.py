class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        while nums:
            left = right = nums.pop()
            while left-1 in nums:
                left -= 1
                nums.remove(left)
                
            while right+1 in nums:
                right += 1
                nums.remove(right)
            
            res = max(res, right-left+1)
        return res