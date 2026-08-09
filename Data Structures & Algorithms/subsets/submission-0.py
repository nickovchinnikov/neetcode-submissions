class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [[]], []
        
        for n in nums:
            i, size = 0, len(res)
            while i < size:
                r = res[i]
                res.append(r[:] + [n])
                i += 1
        return res