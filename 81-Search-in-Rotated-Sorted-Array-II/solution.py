class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right) / 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid+1
                else:
                    right = mid-1
            elif nums[mid] > nums[right]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                right -= 1
        return False