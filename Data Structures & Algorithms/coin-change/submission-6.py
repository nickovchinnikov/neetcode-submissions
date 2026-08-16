class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount+1] * amount
        for am in range(1,amount+1):
            candidates = []
            for coin in coins:
                if am >= coin:
                    dp[am] = min(dp[am], dp[am-coin]+1)
        return dp[-1] if dp[-1] <= amount else -1
                
                
        