class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+":
                right = stack.pop()
                left = stack.pop()
                total = right + left
                stack.extend([left, right, total])
            elif i == "C":
                stack.pop()
            elif i == "D":
                val = stack.pop()
                db = val * 2
                stack.extend([val, db])
            else:
                stack.append(int(i))
        return sum(stack)
