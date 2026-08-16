class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [None] * amount
        for am in range(1,amount+1):
            candidates = []
            for coin in coins:
                needed_coin = am-coin
                if 0 <= needed_coin < len(dp) and dp[needed_coin] is not None:
                    candidates.append(dp[needed_coin]+1)
            dp[am] = min(candidates) if len(candidates) > 0 else None
        return dp[-1] if dp[-1] is not None else -1
                
                
        