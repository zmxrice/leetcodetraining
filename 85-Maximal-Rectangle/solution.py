class Solution(object):
    def getLargestHistogram(self, arr):
        stack = [(0,0)]
        res = 0
        for i in xrange(len(arr)):
            while arr[i] < stack[-1][1]:
                cur = stack.pop()
                res = max(res, cur[1]*(i-stack[-1][0]))
            stack.append((i+1, arr[i]))
        for i in xrange(1,len(stack)):
            cur, pre = stack[i], stack[i-1]
            res = max(res, cur[1]*(stack[-1][0]-pre[0]))
        return res
        
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        cur = map(int,matrix[0])
        candidates = [self.getLargestHistogram(cur)]
        for row in matrix[1:]:
            for i in xrange(len(row)):
                if row[i] == '1':
                    cur[i] += 1
                else:
                    cur[i] = 0
            candidates.append(self.getLargestHistogram(cur))
        return max(candidates)
        