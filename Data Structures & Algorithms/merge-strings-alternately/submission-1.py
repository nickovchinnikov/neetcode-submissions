class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for idx in range(max(len(word1), len(word2))):
            if idx < len(word1):
                res += word1[idx]
            if idx < len(word2):
                res += word2[idx]

        return res
        