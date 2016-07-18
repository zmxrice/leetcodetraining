class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        stack = [(0,0)]
        idx, res = 0, 0
        for height in heights:
            idx += 1
            while height < stack[-1][0]:
                cur = stack.pop()
                res = max(res, (idx - stack[-1][1] - 1)*cur[0])
            stack.append((height, idx))

        for i in xrange(1,len(stack)):
            cur, pre = stack[i], stack[i-1]
            res = max(res, cur[0]*(stack[-1][1]-pre[1]))
            
        return res