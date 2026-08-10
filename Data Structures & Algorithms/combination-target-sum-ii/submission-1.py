class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, subset = [], []

        def dfs(i, total):
            if target == total:
                res.append(subset[:])
                return

            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                if target < total+candidates[j]:
                    break
                subset.append(candidates[j])
                dfs(j+1, total+candidates[j])
                subset.pop()

        dfs(0, 0)
        return res