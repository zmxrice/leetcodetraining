class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n = len(height)
        left, right = [0]*n, [0]*n
        maxLeft = height[0]
        for i in xrange(1,n):
            left[i] = maxLeft
            maxLeft = max(maxLeft, height[i])
        maxRight = height[n-1]
        res = 0
        for i in xrange(n-2, -1, -1):
            right[i] = maxRight
            maxRight = max(maxRight, height[i])
            cur = min(left[i], right[i]) - height[i]
            if cur > 0:
                res += cur
        return res