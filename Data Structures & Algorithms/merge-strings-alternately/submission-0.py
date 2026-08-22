class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_word1 = len(word1)
        len_word2 = len(word2)
        length = (
            len_word1
            if len_word1 > len_word2
            else len_word2
        )

        res = ""
        for idx in range(length):
            if idx < len_word1:
                res += word1[idx]
            if idx < len_word2:
                res += word2[idx]

        return res
        