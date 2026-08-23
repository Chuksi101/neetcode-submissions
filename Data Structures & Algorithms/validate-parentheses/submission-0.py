class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ob = {'(', '[', '{'}
        cb = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in ob:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    opened = stack.pop()
                    if cb[i] != opened:
                        return False
            
        return stack == []