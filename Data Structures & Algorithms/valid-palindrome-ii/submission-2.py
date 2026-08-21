class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
    
        def is_valid(left, right, deleted=False):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    return is_valid(left, right-1, True) or is_valid(left+1, right, True)
                left += 1
                right -= 1
            return True
        
        return is_valid(left, right)
        
        