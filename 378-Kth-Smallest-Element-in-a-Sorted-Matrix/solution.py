import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        heap = []
        rows, cols = len(matrix), len(matrix[0])
        for i in xrange(rows):
            for j in xrange(cols):
                heapq.heappush(heap, matrix[i][j])
                if len(heap) > rows*cols - k+1:
                    heapq.heappop(heap)
        return heap[0]
        