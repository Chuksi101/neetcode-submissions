class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1 for _ in nums]
        result = [0 for _ in nums]
        leftProduct[0] = nums[0]
        for i in range(1, len(nums)):
            leftProduct[i] = nums[i] * leftProduct[i-1]
        rightP = nums[-1]
        result[-1] = leftProduct[len(nums)-2]
        for i in range(len(nums)-2, 0,-1):
            result[i] = leftProduct[i-1] * rightP
            rightP = rightP * nums[i]
        result[0] = rightP
        return result
        