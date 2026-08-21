from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)

        major_elem, counter = 0, 0
        for k,c in counts.items():
            if c > counter:
                counter = c
                major_elem = k
        return major_elem
        