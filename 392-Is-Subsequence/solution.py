class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        if not t:
            return False
        if len(s) > len(t):
            return False
        i, j = 0, 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1

        return j == len(s)