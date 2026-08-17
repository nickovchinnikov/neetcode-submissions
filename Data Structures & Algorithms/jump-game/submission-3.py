class Solution:
    def canJump(self, nums: List[int]) -> bool:
        best = 0
        for i in range(len(nums)):
            if i > best:
                return False
            best = max(best,i+nums[i])
        return True
