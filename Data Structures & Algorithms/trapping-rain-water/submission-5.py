class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts = [0] * len(height)
        max_lefts[0] = height[0]
        for i in range(1, len(height)):
            max_lefts[i] = max(max_lefts[i-1], height[i])
        max_rights = [0] * len(height)
        max_rights[-1] = height[-1]
        for i in range(len(height)-2,-1,-1):
            max_rights[i] = max(max_rights[i+1], height[i])
        vol = 0
        for i, (left, right) in enumerate(zip(max_lefts, max_rights)):
            vol += min(left, right) - height[i]
        return vol
