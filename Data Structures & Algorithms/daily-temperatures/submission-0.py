class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for i in temperatures]
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                curr = stack.pop()
                res[curr[0]] = i - curr[0]
            stack.append((i,temperatures[i]))
                        
        return res
