class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        
        def dfs(x, y):
            if (
                x < 0 or x >= len(grid) or
                y < 0 or y >= len(grid[0])
            ):
                return 0
            
            if (x, y) in visited:
                return 0
            
            visited.add((x, y))
            
            if grid[x][y] == 0:
                return 0
            else:
                return (
                    1 +
                    dfs(x-1, y) +
                    dfs(x+1, y) +
                    dfs(x, y-1) +
                    dfs(x, y+1)
                )
            
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if (x, y) not in visited and grid[x][y] == 1:
                    max_area = max(max_area, dfs(x, y))

        return max_area

