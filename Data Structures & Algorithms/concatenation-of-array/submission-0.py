class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [None for _ in range(len(nums)*2)]
        for i, n in enumerate(nums):
            ans[i] = n
            ans[i+len(nums)] = n
        return ans
        