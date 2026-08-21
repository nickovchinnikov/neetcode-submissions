class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for read in range(1, len(nums)):
            while nums[read-1] == nums[write] and write < len(nums)-1:
                write += 1
            nums[read] = nums[write]
        
        for i, n in enumerate(nums):
            if i+1 == len(nums):
                return len(nums)
            if n == nums[i+1]:
                return i+1


