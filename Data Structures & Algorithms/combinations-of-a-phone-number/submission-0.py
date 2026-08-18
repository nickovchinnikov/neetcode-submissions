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
            # print("start, len(digits): ", start, len(digits))
            if start == len(digits):
                result.append(subset[:])
                # print("result: ", result)
                return

            # print("digits[start]: ", digits[start])
            chars = charmap[int(digits[start])]
            for c in chars:
                subset += c
                # print("subset: ", subset)
                dfs(start+1, subset)
                subset = subset[:-1]

        dfs(0)
        return result
