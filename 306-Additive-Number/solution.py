class Solution(object):
    def helper(self, start, i, j, num):
        if j == len(num):
            return True
        if start < i-1 and num[start] == '0':
            return False
        if i < j-1 and num[i] == '0':
            return False
        tmp = str(int(num[start:i])+int(num[i:j]))
        count = len(tmp)
        if j+count <= len(num) and num[j: j+count] == tmp:
            return self.helper(i,j,j+count, num)
        else:
            return False
            
            
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        n = len(num)
        for i in xrange(1, n):
            for j in xrange(i+1, n):
                if self.helper(0, i, j, num):
                    return True
        return False