class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i, n in enumerate(nums):
            c = target - n
            if c in lookup:
                return [lookup[c], i]
            lookup[n] = i