class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in xrange(len(s)):
            if s[i] in d:
                d[s[i]][1] += 1
            else:
                d[s[i]] = [i, 1]
        for i in s:
            if d[i][1] == 1:
                return d[i][0]
        return -1