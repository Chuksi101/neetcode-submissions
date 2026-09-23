class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = nums[0]
        curMin, curMax = 1, 1

        for n in nums:
            temp = curMax * n
            curMax = max(curMax*n, curMin*n, n)
            curMin = min(temp, curMin*n, n)
            maxP = max(maxP, curMax)
           
        return maxP