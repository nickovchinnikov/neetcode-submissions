class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += f"{len(s)}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == "#":
                start = i+1
                end = start + leng
                dec.append(s[start:end])
                i=end
            else:
                j = i
                while s[j] != "#":
                    j += 1
                leng = int(s[i:j])
                i = j
        return dec

