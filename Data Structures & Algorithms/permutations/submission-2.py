class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
            
        res = []
        subset = []

        def dfs():
            if len(subset) == len(nums):
                res.append(subset[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in subset:
                    continue
                
                subset.append(nums[i])
                dfs()
                subset.remove(nums[i])

        dfs()
        return res

