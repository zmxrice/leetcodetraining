class Solution(object):
    def check(self, s):
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        
    def helper(self, s, res, path):
        if not s:
            res.append(path)
            return
        for i in xrange(1, len(s)+1):
            if self.check(s[:i]):
                self.helper(s[i:], res, path+[s[:i]])
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.helper(s, res, [])
        return res