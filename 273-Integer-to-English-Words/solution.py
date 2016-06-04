class Solution(object):
    def __init__(self):
        self.wordDict = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
    
    def helper(self, num):
        res = []
        if num >= 100:
            res.append(self.wordDict[num/100])
            res.append('Hundred')
        num %= 100
        if 1 <= num <= 20:
            res.append(self.wordDict[num])
            return res
        else:
            if num/10*10:
                res.append(self.wordDict[num/10*10])
            if num%10:
                res.append(self.wordDict[num%10])
        return res
        
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        res = []
        if len(str(num)) > 9:
            res.extend(self.helper(num/10**9))
            res.append('Billion')
            num %= 10**9
        if len(str(num)) > 6:
            res.extend(self.helper(num/10**6))
            res.append('Million')
            num %= 10**6
        if len(str(num)) > 3:
            res.extend(self.helper(num/10**3))
            res.append('Thousand')
            num %= 10**3
        res.extend(self.helper(num))
        return ' '.join(res)