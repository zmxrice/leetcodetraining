class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        if len(triangle) == 1:
            return min(triangle[0])
        cur = triangle[-1]
        for i in xrange(len(triangle)-2, -1, -1):
            next = []
            for j in xrange(len(triangle[i])):
                next.append(min(cur[j], cur[j+1])+triangle[i][j])
            cur = next
        return cur[0]