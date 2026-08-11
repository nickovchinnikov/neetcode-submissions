from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neighbors = (
            (1,0), (-1,0),
            (0,1), (0,-1)
        )

        queue = deque()
        fresh = 0

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 2:
                    queue.append((x,y))
                if grid[x][y] == 1:
                    fresh += 1
        
        mins = 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                x,y = queue.popleft()

                for dx,dy in neighbors:
                    nx,ny = x+dx,y+dy
                    if (
                        nx < 0 or nx >= len(grid) or
                        ny < 0 or ny >= len(grid[nx])
                    ):
                        continue

                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx,ny))
            mins += 1
        
        return mins if fresh == 0 else -1


        