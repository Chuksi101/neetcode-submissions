class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        - initialize dp array
            -> dp = [[0 for _ in range(n)] for _ in range(m)]
        - initialize top row and first column to 1
        for i in range(1,m)
            for j in range(1,n)
        -> recurrence relation: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        - return dp[m-1][n-1]
        '''
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0] = [1]*n
        for i in range(m):
            dp[i][0] = 1

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]