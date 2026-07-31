from collections import defaultdict

class Solution:
    def get_ws_n(self, right, left, maxFreq):
        ws = right - left + 1
        n = ws - maxFreq
        return ws, n
        
    def characterReplacement(self, s: str, k: int) -> int:
        res, maxFreq = 0, 0
        count = defaultdict(int)
        left = 0
        for right in range(len(s)):
            count[s[right]] += 1
            maxFreq = max(maxFreq, count[s[right]])

            windowSize, needed = self.get_ws_n(right, left, maxFreq)

            while needed > k:
                count[s[left]] -= 1
                left += 1

                windowSize, needed = self.get_ws_n(right, left, maxFreq)

            res = max(res, windowSize)

        return res

            