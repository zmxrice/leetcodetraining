class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        preProfit, postProfit = [0]*n, [0]*n
        minVal = prices[0]
        for i in xrange(1, n):
            minVal = min(minVal, prices[i])
            preProfit[i] = max(preProfit[i-1], prices[i]-minVal)
        maxVal = prices[-1]
        for i in xrange(n-2, 0, -1):
            maxVal = max(maxVal, prices[i])
            postProfit[i] = max(postProfit[i+1], maxVal - prices[i])
        profit = 0
        for i in xrange(n):
            profit = max(profit, preProfit[i]+postProfit[i])
        return profit