class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        heights = [0]+heights+[0]
        res = 0
        stack = []
        for i, val in enumerate(heights):
            while stack and val < stack[-1][1]:
                cur = stack.pop()
                res = max(res, (i-stack[-1][0]-1)*cur[1])
            stack.append((i, val))
        return res