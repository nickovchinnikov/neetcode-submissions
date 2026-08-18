class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        charmap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        result = []
        def dfs(start, subset=""):
            if start == len(digits):
                result.append(subset)
                return

            chars = charmap[int(digits[start])]
            for c in chars:
                dfs(start+1, subset + c)

        dfs(0)
        return result
