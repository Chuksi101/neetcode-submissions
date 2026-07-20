class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]
        leftP = rightP = 1
        for i in range(len(nums)):
            result[i] = leftP
            leftP *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            result[i] *= rightP
            rightP *= nums[i]
        return result
        