class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right, prev_mid = 0, len(nums), -1

        while left < right:
            mid = (left + right) // 2
            if mid == prev_mid:
                return -1
            elif nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid
            elif target < nums[mid]:
                right = mid
            prev_mid = mid
        return -1

