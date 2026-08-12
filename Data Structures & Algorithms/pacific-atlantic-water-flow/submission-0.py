from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = (
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
        )

        flow2pacific = [[False]*len(row) for row in heights]

        queue = deque()

        # Pacific started positions
        for x in range(len(heights)):
           queue.append((x, 0))
           flow2pacific[x][0] = True
        for y in range(len(heights[0])):
            queue.append((0, y))
            flow2pacific[0][y] = True

        visited = set(queue)

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
                    flow2pacific[nx][ny] = True
                    queue.append((nx,ny))

        flow2atlantic = [[False]*len(row) for row in heights]

        queue = deque()

        # Pacific started positions
        for x in range(len(heights)):
            y = len(heights[0])-1
            queue.append((x, y))
            flow2atlantic[x][y] = True
        for y in range(len(heights[0])):
            x = len(heights)-1
            queue.append((x, y))
            flow2atlantic[x][y] = True
        
        visited = set(queue)

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
                    flow2atlantic[nx][ny] = True
                    queue.append((nx,ny))
        
        result = []
        for x in range(len(flow2pacific)):
            for y in range(len(flow2pacific[x])):
                if flow2pacific[x][y] and flow2atlantic[x][y]:
                    result.append([x,y])
        return result



