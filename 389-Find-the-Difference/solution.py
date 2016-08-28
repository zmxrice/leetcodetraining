class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for i in xrange(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            if t[i] not in d:
                d[t[i]] = -1
            else:
                d[t[i]] -= 1
        if t[-1] not in d:
            d[t[-1]] = -1
        else:
            d[t[-1]] -= 1
        for key, val in d.items():
            if val != 0:
                return key