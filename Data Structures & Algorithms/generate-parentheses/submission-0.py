class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opened, closed, subset):
            if opened > n or closed > n:
                return

            if opened == closed and len(subset) == 2*n:
                res.append(subset)
                return
            
            dfs(opened+1, closed, subset + "(")

            if opened > closed:
                dfs(opened, closed+1, subset + ")")
            
        dfs(0, 0, "")
        return res
