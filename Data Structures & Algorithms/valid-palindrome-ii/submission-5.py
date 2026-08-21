class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
    
        def is_pal(left, right, deleted=False):
            while left < right:
                if s[left] != s[right]:
                    if deleted:
                        return False
                    return is_pal(left, right-1, True) or is_pal(left+1, right, True)
                left += 1
                right -= 1
            return True
        
        return is_pal(left, right)
        
        