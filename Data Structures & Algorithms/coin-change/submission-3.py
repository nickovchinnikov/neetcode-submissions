class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins_set = set(coins)
        dp = [0] + [None] * amount
        # coins=[1,2,5]
        for am in range(1,amount+1):
            # print("am: ", am)
            if am in coins_set:
                dp[am] = 1
                # print("dp: ", dp)
                # print()
                continue
            candidates = []
            for coin in coins:
                needed_coin = am-coin
                # print("needed_coin:", needed_coin)
                if 0 < needed_coin < len(dp) and dp[needed_coin] is not None:
                    candidates.append(dp[needed_coin]+1)
            # print("candidates: ", candidates)
            # if len(candidates) == 0:
            #     return -1
            dp[am] = min(candidates) if len(candidates) > 0 else None
        #     print("dp: ", dp)
        #     print()
        # print("dp_final: ", dp)
        return dp[-1] if dp[-1] is not None else -1
                
                
        