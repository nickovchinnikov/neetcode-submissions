class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = {n: i for i, n in enumerate(numbers)}
        for i, n in enumerate(numbers):
            if target-n in s and s[target-n] != i:
                return [i+1, s[target-n]+1]

        