from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        INF = 2147483647
        directions = (
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        )

        queue = deque()

        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    queue.append((x,y))
        
        while queue:
            x,y = queue.popleft()

            for dx, dy in directions:
                nx=x+dx
                ny=y+dy

                if (
                    nx < 0 or nx >= len(grid) or
                    ny < 0 or ny >= len(grid[nx])
                ):
                    continue

                if grid[nx][ny] == INF:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx,ny))


