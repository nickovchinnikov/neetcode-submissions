class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        def is_pal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                return is_pal(left+1, right) or is_pal(left, right-1)
            left += 1
            right -= 1
        return True