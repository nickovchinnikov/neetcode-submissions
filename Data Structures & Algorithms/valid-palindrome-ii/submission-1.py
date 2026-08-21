class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        self.replaced = 0
    
        def is_valid(left, right):
            while left < right:
                if s[left] != s[right]:
                    if self.replaced > 0:
                        return False
                    self.replaced += 1
                    if not is_valid(left, right-1) and not is_valid(left+1, right):
                        return False
                    return True
                left += 1
                right -= 1
            return True
        
        return is_valid(left, right)
        
        