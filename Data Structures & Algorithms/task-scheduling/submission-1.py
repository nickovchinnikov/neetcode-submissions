from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # [X, X], n=2
        # X--X => len * n
        # [X, X, X, X]
        # X--X--X--X => (len-1) * (n+1) + 1
        # [X, X, Y, Y]
        # XY-XY => (len-1) * (n+1) + k
        # [X, X, Y, Y, Z, Z]
        # XYZXYZXYZ => len(tasks)
        counter = Counter(tasks)

        maxFreq = max(counter.values())
        maxCount = sum(v == maxFreq for v in counter.values())

        return max(
            len(tasks),
            (maxFreq-1) * (n+1) + maxCount,
        )

