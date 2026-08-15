class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        neighboth = (
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
        )

        visited = set()

        def dfs(x,y,depth):
            if (x,y) in visited:
                return False

            visited.add((x,y))

            if board[x][y] != word[depth]:
                visited.remove((x,y))
                return False

            if depth == len(word)-1:
                return True
            
            level = []
            for dx,dy in neighboth:
                xn = x+dx
                yn = y+dy

                if (
                    xn < 0 or xn > len(board)-1 or
                    yn < 0 or yn > len(board[x])-1
                ):
                    continue
                
                level.append(dfs(xn,yn,depth+1))
            visited.remove((x,y))
            return any(level)

        # Find start and run
        for x, row in enumerate(board):
            for y, cell in enumerate(row):
                if cell == word[0]:
                    if dfs(x,y,0):
                        return True
        
        return False


