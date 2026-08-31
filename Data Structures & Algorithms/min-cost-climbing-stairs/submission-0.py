class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0]* (len(cost)+1)

        i = 2
        while i <= len(cost):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1]+cost[i-1])
            i += 1

        return dp[-1]