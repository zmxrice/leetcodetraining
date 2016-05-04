class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        left, right = 0, x
        while left < right:
            mid = (left+right)/2
            if mid ** 2 > x:
                if (mid-1)**2 <= x:
                    return mid-1
                else:
                    right = mid-1
            elif mid ** 2 < x:
                if (mid+1)**2 == x:
                    return mid+1
                elif (mid+1)**2 > x:
                    return mid
                else:
                    left = mid+1
            else:
                return mid