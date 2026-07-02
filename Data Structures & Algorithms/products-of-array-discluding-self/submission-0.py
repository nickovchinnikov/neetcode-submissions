class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        for i, n in enumerate(nums[:-1]):
            left.append(left[i] * n)
        right = [1]
        for i, n in enumerate(reversed(nums[1:])):
            right.append(right[i] * n)
        right = reversed(right)
        res = []
        for l, r in zip(left, right):
            res.append(l*r)
        return res
