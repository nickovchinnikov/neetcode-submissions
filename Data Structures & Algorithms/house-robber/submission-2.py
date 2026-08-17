class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        dp = [
            nums[0],
            max(nums[0],nums[1])
        ] 
        dp += [0] * (len(nums)-2)
        print("dp: ", dp)
        # [2,9,8,3,6]
        for i,n in enumerate(nums[2:],start=2):
            print("i, n: ", i, n)
            dp[i] = max(
                dp[i-2]+n,
                dp[i-1]
            )
            print("dp: ", dp)
            print()
        return max(dp[-2],dp[-1])


