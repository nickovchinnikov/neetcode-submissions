from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        heap = []
        for count in counter.values():
            heapq.heappush(heap, -count)
        
        queue = deque()
        time = 0

        while heap or queue:
            time += 1

            if heap:
                c = heapq.heappop(heap)
                c += 1

                if c != 0:
                    queue.append((c, time+n))
            
            if queue and queue[0][1] == time:
                c, _ = queue.popleft()
                heapq.heappush(heap, c)         

        return time

