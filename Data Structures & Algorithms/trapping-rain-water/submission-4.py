class Solution:
    def trap(self, height: List[int]) -> int:
        max_lefts, max_rights = [], []
        for i in range(len(height)):
            max_left, l = 0, i
            while l >= 0:
                max_left = max(max_left, height[l])
                l -= 1
            max_right, r = 0, i
            while r < len(height):
                max_right = max(max_right, height[r])
                r += 1
            max_rights.append(max_right)
            max_lefts.append(max_left)
        
        vol = 0
        for i, (left, right) in enumerate(zip(max_lefts, max_rights)):
            vol += min(left, right) - height[i]
        return vol
            
        