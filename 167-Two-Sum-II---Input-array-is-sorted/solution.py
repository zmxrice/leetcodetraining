class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while left < right:
            cur = numbers[left] + numbers[right]
            if cur < target:
                left += 1
            elif cur > target:
                right -= 1
            else:
                return [left+1, right+1]
        return [-1,-1]