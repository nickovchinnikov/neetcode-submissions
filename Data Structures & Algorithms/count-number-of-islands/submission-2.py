class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()

        def dfs(x, y):
            if(
                x < 0 or x >= len(grid) or
                y < 0 or y >= len(grid[0])
            ):
                return

            if (x, y) in visited:
                return
            
            # Visited
            visited.add((x, y))

            if grid[x][y] == "0":
                return
            
            if grid[x][y] == "1":
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) not in visited and grid[x][y] == "1":
                    res += 1
                    dfs(x, y)
        
        return res


