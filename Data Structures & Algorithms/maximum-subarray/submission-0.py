class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Look up Kadane's Alg
        '''
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0) + n
            maxSum = max(curSum, maxSum)

        return maxSum
