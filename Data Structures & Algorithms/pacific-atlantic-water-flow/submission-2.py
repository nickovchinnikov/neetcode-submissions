from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = (
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
        )

        def bfs(queue, visited):
            while queue:
                x,y = queue.popleft()

                for dx,dy in directions:
                    nx,ny = x+dx,y+dy

                    if (
                        nx < 0 or nx >= len(heights) or
                        ny < 0 or ny >= len(heights[0])
                    ):
                        continue

                    if (nx,ny) not in visited and heights[x][y] <= heights[nx][ny]:
                        visited.add((nx,ny))
                        queue.append((nx,ny))
        
        queue_pacific = deque()

        # Pacific started positions
        for x in range(len(heights)):
           queue_pacific.append((x, 0))
        for y in range(len(heights[0])):
            queue_pacific.append((0, y))

        visited_pacific = set(queue_pacific)

        bfs(queue_pacific, visited_pacific)

        queue_atlantic = deque()

        # Pacific started positions
        for x in range(len(heights)):
            y = len(heights[0])-1
            queue_atlantic.append((x, y))
        for y in range(len(heights[0])):
            x = len(heights)-1
            queue_atlantic.append((x, y))
        
        visited_atlantic = set(queue_atlantic)

        bfs(queue_atlantic, visited_atlantic)

        return [[x,y] for x,y in visited_pacific & visited_atlantic]






