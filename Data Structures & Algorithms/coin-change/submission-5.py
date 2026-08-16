class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [amount+1] * amount
        for am in range(1,amount+1):
            candidates = []
            for coin in coins:
                needed_coin = am-coin
                if needed_coin >= 0 and dp[needed_coin] <= amount:
                    candidates.append(dp[needed_coin]+1)
            if len(candidates) > 0:
                dp[am] = min(candidates)
        return dp[-1] if dp[-1] <= amount else -1
                
                
        