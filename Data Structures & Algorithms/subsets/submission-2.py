class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            # When this's over append
            if i == len(nums):
                res.append(subset[:])
                return
            
            # current subset loop
            backtrack(i + 1)
            # add one more
            subset.append(nums[i])
            # one more loop
            backtrack(i + 1)
            subset.pop()

        backtrack(0)
        return res
        