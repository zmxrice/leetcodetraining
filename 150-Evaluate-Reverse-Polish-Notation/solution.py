class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        ops = {"+": lambda x, y: x+y, "-": lambda x, y: x-y, "*": lambda x, y: x*y, "/": lambda x, y: x/y}
        for token in tokens:
            if token in "+-*/":
                right = stack.pop()
                stack[-1] = int(ops[token](stack[-1], float(right)))
            else:
                stack.append(int(token))
        return stack[-1]
        