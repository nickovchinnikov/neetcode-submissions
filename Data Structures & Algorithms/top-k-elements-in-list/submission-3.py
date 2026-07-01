import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for n in nums:
            d[n] += 1
        
        heap = []

        for n, count in d.items():
            heapq.heappush(heap, (count, n))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [n for _, n in heap]

