class Solution:
    def trap(self, height: List[int]) -> int:
        vol = 0
        for i in range(len(height)):
            max_left = height[i]
            l = i
            while l >= 0:
                max_left = max(max_left, height[l])
                l -= 1
            
            max_right = height[i]
            r = i
            while r < len(height):
                max_right = max(max_right, height[r])
                r += 1
            
            vol += min(max_left, max_right) - height[i]

        return vol
                
        