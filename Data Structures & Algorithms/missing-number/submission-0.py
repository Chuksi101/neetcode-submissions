class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        store = set(nums)
        for i in range(len(nums)+1):
            if i not in store:
                return i
