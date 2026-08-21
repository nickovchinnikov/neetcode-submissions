class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = 0
        majority = 0

        for n in nums:
            if counts == 0:
                majority = n
            
            if majority == n:
                counts += 1
            else:
                counts -= 1
        return majority
