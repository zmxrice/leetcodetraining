class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        n = len(ratings)
        if n == 1:
            return 1
        left, right = [0]*n, [0]*n
        left[0] = 1
        for i in xrange(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
            else:
                left[i] = 1
        res = right[n-1] = left[n-1]
        for i in xrange(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1]+1
            else:
                right[i] = 1
            res += max(left[i], right[i])
        return res
            