from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, res, maxFreq = 0, 0, 0
        count = defaultdict(int)
        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])

            while right - left + 1 - maxFreq > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res

            