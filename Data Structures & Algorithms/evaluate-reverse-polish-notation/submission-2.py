class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+','-','*','/'}
        for i in tokens:
            if i not in operands:
                stack.append(int(i))
            else:
                r = stack.pop()
                l = stack.pop()
                res = 0
                if i == '+':
                    res = l+r
                elif i == '-':
                    res = l - r
                elif i == '*':
                    res = l * r
                else:
                    res = int(l / r)
                stack.append(res)
        
        return stack[-1]