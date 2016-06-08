class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        left, right = 0, n-1
        while left < right:
            mid = (left+right) / 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]
                
            