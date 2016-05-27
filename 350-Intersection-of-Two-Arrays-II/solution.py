class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1, d2 = {}, {}
        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1
        res = []
        for key, val in d1.items() :
            if key in d2:
                for i in xrange(min(val,d2[key])):
                    res.append(key)
        return res