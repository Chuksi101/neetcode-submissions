class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        if n == 1:
            return 1
        elif n == 2:
            return 2
        dp[1], dp[2] = 1,2

        def rec(i,arr):
            if arr[i] > 0:
                return arr[i]

            arr[i] = rec(i-1, arr) + rec(i-2, arr)
            return arr[i]

        return rec(n, dp)