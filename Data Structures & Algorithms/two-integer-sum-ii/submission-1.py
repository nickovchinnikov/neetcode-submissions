class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {}
        for i, n in enumerate(numbers):
            if target-n in s:
                return [s[target-n]+1,i+1]
            s[n] = i

        