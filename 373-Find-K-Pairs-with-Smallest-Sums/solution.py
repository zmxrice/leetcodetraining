import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if len(nums1) * len(nums2) < k:
            return [[i, j] for i in nums1 for j in nums2]
        heap = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(heap, [i+j, i, j])
        res = []
        for i in xrange(k):
            cur = heapq.heappop(heap)
            res.append([cur[1], cur[2]])
        return res