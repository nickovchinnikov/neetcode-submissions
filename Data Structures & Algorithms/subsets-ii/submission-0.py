class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, subset = [], []
        print(nums)
        def dfs(i):
            res.append(subset[:])
            for j in range(i, len(nums)):
                if j > i and nums[j-1] == nums[j]:
                    continue
                subset.append(nums[j])
                dfs(j+1)
                subset.pop()

        dfs(0)
        return res

