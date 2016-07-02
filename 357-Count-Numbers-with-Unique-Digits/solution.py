class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        res = 10
        for i in xrange(2, n+1):
            cur = 9
            for j in xrange(i-1):
                cur *= 9-j
            res += cur
        return res