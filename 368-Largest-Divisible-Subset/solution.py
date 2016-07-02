class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        dp = {-1:[]}
        for i in nums:
            dp[i] = max((dp[x] for x in dp if i % x == 0), key=len) + [i]
        return max(dp.values(), key=len)
                        