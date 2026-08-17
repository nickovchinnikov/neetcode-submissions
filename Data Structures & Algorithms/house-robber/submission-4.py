class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prv,nxt = 0,0

        for n in nums:
            nxt,prv = prv,max(prv,nxt+n)

        return prv
