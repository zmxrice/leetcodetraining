class Solution(object):
    def check(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def helper(self, s, res, path, idx):
        if idx >= len(s):
            res.append(path)
            return
        for i in xrange(idx+1, len(s)+1):
            if self.check(s[idx:i]):
                self.helper(s, res, path+[s[idx:i]], i)
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(s, res, [], 0)
        return res