class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water, left, right = 0, 0, len(heights)-1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            if height == heights[left]:
                left += 1
            else:
                right -= 1
            max_water = max(max_water, width * height)
        return max_water
        