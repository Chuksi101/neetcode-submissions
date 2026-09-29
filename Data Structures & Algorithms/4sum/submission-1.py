class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        if len(nums) < 4:
            return res
        for a in range(len(nums)-3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a+1, len(nums)-2):
                if b > a+1 and nums[b] == nums[b - 1]:
                    continue
                c,d = b+1, len(nums)-1
                while c < d:
                    print(a,b,c,d)
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total < target:
                        c += 1
                    elif total > target:
                        d -= 1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1

        return res