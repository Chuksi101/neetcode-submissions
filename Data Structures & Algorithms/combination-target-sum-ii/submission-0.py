class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(path, left, i):
            if left == 0:
                res.append(path[:])
                return
                
            if i >= len(candidates) or left < 0:
                return
            path.append(candidates[i])
            dfs(path, left-candidates[i], i + 1)
            path.pop()
            while i < len(candidates)-1 and candidates[i+1]==candidates[i]:
                i +=1
            dfs(path, left, i + 1)

        dfs([], target, 0)
        return res