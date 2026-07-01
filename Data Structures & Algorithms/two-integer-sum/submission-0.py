class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        for i, n in enumerate(nums):
            c = target - n
            i0 = lookup.get(c, -1)
            if i0 >= 0:
                return [i0, i]
            lookup[n] = i