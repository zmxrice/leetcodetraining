class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d = {}
        for i in ransomNote:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in magazine:
            if i in d:
                d[i] -= 1
        for val in d.values():
            if val > 0:
                return False
        return True