
# i      0      1                   2                        3
# cost   1     100                  1                        1
# dp     1     100     dp[i-2]+cost[i]=>1+1=[2]      dp[i-2]+cost[i]=>100+1=101
#                      dp[i-1]+cost[i]=>100+1=101    dp[i-1]+cost[i]=>2+1=[3]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [None] * len(cost)
        dp[0],dp[1] = cost[0],cost[1]

        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2], dp[i-1])+cost[i]

        return min(dp[-1],dp[-2])
