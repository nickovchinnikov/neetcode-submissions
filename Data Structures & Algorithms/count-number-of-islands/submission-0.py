class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = []
        visited = set()
        island = set()

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
                island.add((x, y))
                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)
            else:
                visited.add((x1, y1))
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if (x, y) in visited:
                    continue
                
                if grid[x][y] == "0":
                    visited.add((x, y))
                    continue

                if grid[x][y] == "1":
                    dfs(x, y)
                
                if island:
                    res.append(list(island))
                    island = set()
        
        return len(res)
        