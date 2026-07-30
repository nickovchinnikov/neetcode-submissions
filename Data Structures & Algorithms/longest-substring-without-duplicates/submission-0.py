class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, best, subst = 0, 0, set()
        for right in range(len(s)):
            while s[right] in subst:
                subst.remove(s[left])
                left += 1
            subst.add(s[right])
            best = max(best, right - left + 1)
        return best