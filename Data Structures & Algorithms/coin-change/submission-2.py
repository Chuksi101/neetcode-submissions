class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = float('inf')
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0

        for total in range(1, amount+1):
            for c in coins:
                if (total - c) >= 0:
                    dp[total] = min(dp[total], 1 + dp[total-c])
        
        return -1 if type(dp[-1]) == float else dp[-1]