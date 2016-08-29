class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [(0,0)]
        res = 0
        for i in xrange(len(heights)):
            while heights[i] < stack[-1][1]:
                cur = stack.pop()
                res = max(res, cur[1]*(i-stack[-1][0]))
            stack.append((i+1, heights[i]))
        #deal with the last item
        for i in xrange(1, len(stack)):
            cur, pre = stack[i], stack[i-1]
            res = max(res, cur[1]*(stack[-1][0]-pre[0]))
        return res