class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        
        for c in t:
            count = counter.get(c, 0) - 1
            if count == -1:
                return False
            counter[c] = count
            
        return True