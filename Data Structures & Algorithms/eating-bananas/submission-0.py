class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left+right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid
            
            if hours > h:
                left = mid+1
            else:
                right = mid
        
        return left

