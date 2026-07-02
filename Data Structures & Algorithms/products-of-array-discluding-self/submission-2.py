class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * len(nums), [1] * len(nums)
        for i, (nl, nr) in enumerate(zip(nums[:-1], reversed(nums[1:]))):
            left[i+1] = left[i] * nl
            right[i+1] = right[i] * nr
        right = reversed(right)
        res = []
        for l, r in zip(left, right):
            res.append(l*r)
        return res
