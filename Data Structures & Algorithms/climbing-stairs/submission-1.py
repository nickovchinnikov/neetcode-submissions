class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        dp = [None] * n

        dp[0],dp[1] = 1,2

        i = 2
        while i < n:
            dp[i] = dp[i-1] + dp[i-2]
            i += 1

        return dp[-1]