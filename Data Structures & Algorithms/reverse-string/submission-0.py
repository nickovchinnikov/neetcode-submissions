class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left, right = 0, len(s)-1

        while left < right:
            char_left, char_right = s[left], s[right]
            s[left] = char_right
            s[right] = char_left

            left += 1
            right -= 1

        