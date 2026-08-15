class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opened, closed, subset):
            if len(subset) == 2*n:
                res.append(subset)
                return
            
            if opened < n:
                dfs(opened+1, closed, subset + "(")

            if closed < opened:
                dfs(opened, closed+1, subset + ")")
            
        dfs(0, 0, "")
        return res
