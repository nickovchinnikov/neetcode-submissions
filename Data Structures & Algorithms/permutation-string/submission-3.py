from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = defaultdict(int)
        for c in s1:
            d1[c] += 1

        d2 = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            d2[s2[right]] += 1
            if len(s1) < right - left + 1:
                d2[s2[left]] -= 1
                if d2[s2[left]] <= 0:
                    del d2[s2[left]]
                left += 1

            if right - left + 1 == len(s1) and d1 == d2:
                return True
        
        return False
