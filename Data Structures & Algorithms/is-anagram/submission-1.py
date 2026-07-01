class Solution:
    def to_dict(self, s) -> dict:
        res = {}
        for c in s:
            res[c] = res.get(c, 0) + 1
        return res

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ds = self.to_dict(s)
        dt = self.to_dict(t)
        return ds == dt
