class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        m, n = len(word1)+1, len(word2)+1
        matrix = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(n):
            matrix[0][i] = i
        for j in xrange(m):
            matrix[j][0] = j
        
        for i in xrange(1, m):
            for j in xrange(1, n):
                matrix[i][j] = min(matrix[i-1][j-1]+(word1[i-1] != word2[j-1]), 1+matrix[i-1][j], 1+matrix[i][j-1])
        return matrix[-1][-1]