class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right)/2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid+1
            else:
                right -= 1
        return nums[left]