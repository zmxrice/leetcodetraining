class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        dp = [1]*(n+1)
        dp[2] = 2
        dp[3] = 3
        dp[4] = 4
        for i in xrange(5, n+1):
            dp[i] = dp[i-3]*3
        if dp[-1] > 2**31-1:
            return 2**31-1
        return dp[-1]