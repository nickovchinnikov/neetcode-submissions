from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)

        if "0000" in deadends_set:
            return -1

        def get_neighbors(comb: str):
            neighbors = []
            for i,v in enumerate(comb):
                c = int(v)
                up = (c+1) % 10
                down = (c-1) % 10
                neighbors.append(f"{comb[:i]}{up}{comb[i+1:]}")
                neighbors.append(f"{comb[:i]}{down}{comb[i+1:]}")

            return neighbors
        
        start = "0000"
        visited, queue = {start}, deque([(start, 0)])

        while queue:
            comb, distance = queue.popleft()

            if comb == target:
                return distance
            
            for neighbor in get_neighbors(comb):
                if neighbor not in visited and neighbor not in deadends_set:
                    visited.add(neighbor)
                    queue.append((neighbor, distance+1))
        
        return -1

