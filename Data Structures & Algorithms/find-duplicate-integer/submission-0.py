class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        checker = set()

        for n in nums:
            if n in checker:
                return n
            checker.add(n)
        