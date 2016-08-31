class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        d = {}
        def dfs(s):
            res = []
            if s in wordDict:
                res.append(s)
            for i in xrange(1, len(s)):
                prefix, sufix = s[:i], s[i:]
                if prefix in wordDict:
                    tmp = []
                    if sufix in d:
                        tmp = d[sufix]
                    else:
                        tmp = dfs(sufix)
                    for t in tmp:
                        res.append(prefix+" "+t)
            d[s] = res
            return res
        return dfs(s)
                