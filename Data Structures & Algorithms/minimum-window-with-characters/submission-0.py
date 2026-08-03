from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = defaultdict(int)

        for c in t:
            d1[c] += 1
        
        d2 = defaultdict(int)
        left, have, best_left, best_len = 0, 0, 0, float('inf')
        
        for right in range(len(s)):
            c = s[right]
            d2[c] += 1
            
            if c in d1 and d1[c] >= d2[c]:
               have += 1
            
            while have == len(t):
                if right - left + 1 < best_len:
                    best_left = left
                    best_len = right - left + 1

                cl = s[left]
                d2[cl] -= 1

                if cl in d1 and d2[cl] < d1[cl]:
                    have -= 1
                left += 1
        
        if best_len == float("inf"):
            return ""
        
        return s[best_left:best_left+best_len]

