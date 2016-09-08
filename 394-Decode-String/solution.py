class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        nums = []
        num = ""
        res = ""
        i = 0
        while i < len(s):
            if not s[i].isdigit():
                res += s[i]
                i += 1
            else:
                break
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
            elif s[i] == ']':
                tmp = ""
                while stack and stack[-1] != "[":
                    tmp = stack.pop()+tmp
                if stack and stack[-1] == '[':
                    stack.pop()
                stack.append(nums.pop()*tmp)
                
            elif s[i] == '[':
                stack.append(s[i])
                nums.append(int(num))
                num = ""
            else:
                stack.append(s[i])
            i += 1
        if stack:
            res += ''.join(stack)
        return res
                
                    