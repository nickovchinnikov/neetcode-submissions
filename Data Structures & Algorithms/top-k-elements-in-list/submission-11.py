from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        for n, c in counts.items():
            buckets[c].append(n)

        res = []
        for b in reversed(buckets):
            if len(b) > 0:
                res += b
            if len(res) >= k:
                return res[:k]

        return res