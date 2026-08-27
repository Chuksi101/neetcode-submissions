class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def backtrack(path, i, remaining):
            '''
            '''
            if i == n or nums[i] > remaining:
                return
            path.append(nums[i])
            remaining -= nums[i]

            if remaining == 0:
                res.append(path[:])
                path.pop()
                return
            
            backtrack(path, i, remaining)
            path.pop()
            backtrack(path, i+1, remaining + nums[i])

        backtrack([],0,target)
        return res
