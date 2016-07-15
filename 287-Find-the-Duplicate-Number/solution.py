class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums)
        while left < right:
            mid = (left+right) / 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count > mid:
                right = mid
            else:
                left = mid+1
        return left