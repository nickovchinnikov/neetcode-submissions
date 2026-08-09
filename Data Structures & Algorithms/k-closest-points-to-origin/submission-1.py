import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            x, y = p[0], p[1]
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        return [[x, y] for _, x, y in heap]
