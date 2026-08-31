class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        initialize a dp array with len(nums)
        dp[0] and dp[1] should be set
        i = 2
        while i < len(nums):
            i can either rob today and next tomorrow
            or not today and rob tomorrow
            invariant for dp[i]: max(nums[i],dp[i-1]) 
        '''
        if len(nums) < 2:
            return nums[0]
        dp = [0 for _ in nums]
        dp[0], dp[1] = nums[0], max(nums[1],nums[0])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2],dp[i-1])

        return dp[-1]