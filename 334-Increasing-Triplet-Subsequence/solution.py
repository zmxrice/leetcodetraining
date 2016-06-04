class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        minVal = nums[0]
        minMid = None
        for i in xrange(1, len(nums)):
            if nums[i] <= minVal:
                minVal = nums[i]
            elif not minMid is None and minMid < nums[i]:
                return True
            elif not minMid is None:
                minMid = min(minMid, nums[i])
            else:
                minMid = nums[i]
        return False