class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        res = [0,1]
        count = 1
        while 2**count <= num:
            count += 1
        for i in xrange(count-2):
            tmp = []
            for j in res:
                tmp.append(j+1)
            res.extend(tmp)
        tmp = []
        for i in xrange(num-2**(count-1)+1):
            tmp.append(res[i]+1)
        res.extend(tmp)
        return res