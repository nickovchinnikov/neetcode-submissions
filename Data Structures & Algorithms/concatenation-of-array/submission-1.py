class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [None for _ in range(length*2)]
        for i, n in enumerate(nums):
            ans[i] = n
            ans[i+length] = n
        return ans
        