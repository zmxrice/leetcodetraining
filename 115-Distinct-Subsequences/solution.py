class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s:
            return 0
        if not t:
            return 1
        if len(t) > len(s):
            return 0
        dp = [[0 for j in xrange(len(s))] for i in xrange(len(t))]
        if s[0] == t[0]:
            dp[0][0] = 1
        for j in xrange(1,len(s)):
            dp[0][j] = dp[0][j-1]
            if s[j] == t[0]:
                dp[0][j] += 1
        for i in xrange(1, len(t)):
            for j in xrange(i,len(s)):
                dp[i][j] = dp[i][j-1]
                if t[i] == s[j]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[-1][-1]
                
                
        
                