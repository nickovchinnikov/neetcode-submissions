class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        best = curr = jumps = 0
        for i in range(len(nums)-1):
            best = max(best, i+nums[i])
            if i == curr:
                curr = best
                jumps += 1
                if best >= len(nums)-1:
                    return jumps
        