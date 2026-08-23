class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        INF = float("inf")
        answer, left, subsum = INF, 0, 0

        for right in range(len(nums)):
            subsum += nums[right]

            while subsum >= target:
                answer = min(answer, right-left+1)
                subsum -= nums[left]
                left += 1

        return answer if answer != INF else 0