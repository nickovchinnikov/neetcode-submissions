class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res, stack = [0] * len(temperatures), []

        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()
                res[prev] = idx - prev
            stack.append(idx)
            
        return res

