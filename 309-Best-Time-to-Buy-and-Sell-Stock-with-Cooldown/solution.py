class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0
        buy, sell = [0]*n, [0]*n
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, prices[1]-prices[0])
        for i in xrange(2, n):
            buy[i] = max(buy[i-1], sell[i-2]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        return sell[-1]