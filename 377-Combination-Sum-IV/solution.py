class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0]*(target+1)
        nums = sorted(nums)
        pool = set(nums)
        if nums[0] > target:
            return 0
        for i in xrange(nums[0], target+1):
            if i in pool:
                dp[i] += 1
            for j in nums:
                if i - j > 0:
                    if dp[i-j] != 0:
                        dp[i] += dp[i-j]
                else:
                    break
        return dp[target]