class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]
        for i, (nl, nr) in enumerate(zip(nums[:-1], reversed(nums[1:]))):
            left.append(left[i] * nl)
            right.append(right[i] * nr)
        right = reversed(right)
        res = []
        for l, r in zip(left, right):
            res.append(l*r)
        return res
