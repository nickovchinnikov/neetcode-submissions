class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        result, subset = [], []
        
        def dfs(start):
            if start == len(s):
                result.append(subset[:])

            for end in range(start, len(s)):
                sub = s[start:end+1]
                if is_palindrome(sub):
                    subset.append(sub)
                    dfs(end+1)
                    subset.pop()

        dfs(0)
        return result
