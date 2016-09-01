class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start, end = 0, 0
        res = 0
        while end < len(s):
            if s[end] in d:
                res = max(res, end-start)
                start = max(start, d[s[end]]+1)
            d[s[end]] = end
            end += 1
        return max(res, end-start)