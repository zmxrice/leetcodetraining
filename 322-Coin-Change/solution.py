class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0]*(amount+1)
        for i in xrange(amount+1):
            candidates = []
            for coin in coins:
                if i >= coin:
                    candidates.append(dp[i-coin]+1)
            dp[i] = max(candidates)
        if dp[-1] == 0:
            return -1
        else:
            return dp[-1]