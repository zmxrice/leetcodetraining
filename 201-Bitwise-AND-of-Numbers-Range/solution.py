class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        gap = n-m+1
        binM, binN = bin(m)[2:], bin(n)[2:]
        lenM, lenN = len(binM)-1, len(binN)-1
        count, res = 0, 0
        while lenM >= 0 and lenN >= 0:
            if binM[lenM] == binN[lenN] == '1' and 2**count >= gap:
                res += 2**count
            count += 1
            lenM -= 1
            lenN -= 1
        return res