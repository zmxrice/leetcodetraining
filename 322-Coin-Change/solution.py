class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [0]*(amount+1)
        for i in xrange(amount+1):
            candidates = []
            for coin in coins:
                if i > coin:
                    if dp[i-coin] != -1:
                        candidates.append(dp[i-coin]+1)
                elif i == coin:
                     candidates.append(1)
            if candidates:
                dp[i] = min(candidates)
            else:
                dp[i]=-1
     
        return dp[-1]