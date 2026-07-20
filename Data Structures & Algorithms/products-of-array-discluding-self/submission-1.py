class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in nums]
        result[0] = leftP = nums[0]
        for i in range(1, len(nums)-1):
            result[i] = nums[i] * result[i-1]
            leftP = leftP * nums[i]
        result[-1] = leftP
        rightP = nums[-1]
        for i in range(len(nums)-2, 0,-1):
            result[i] = result[i-1] * rightP
            rightP = rightP * nums[i]
        result[0] = rightP
        return result
        