class Solution(object):
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)
        
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        return z == 0 or (z-x <= y and z % self.gcd(x,y) == 0)