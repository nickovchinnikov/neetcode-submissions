from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = (
            (1,0),
            (-1,0),
            (0,1),
            (0,-1),
        )

        def bfs(x, y):
            queue = deque()
            queue.append((x,y))
            board[x][y] = "#"
            while queue:
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx,y+dy

                    if (
                        nx < 0 or nx >= len(board) or
                        ny < 0 or ny >= len(board[nx])
                    ):
                        continue

                    if board[nx][ny] == "O":
                        board[nx][ny] = "#"
                        queue.append((nx,ny))

        for x in range(len(board)):
            if board[x][0] == "O":
                bfs(x,0)
            
            y = len(board[x])-1
            if board[x][y] == "O":
                bfs(x,y)
        
        for y in range(len(board[0])):
            if board[0][y] == "O":
                bfs(0,y)
            
            x = len(board)-1
            if board[x][y] == "O":
                bfs(x,y)
        
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == "O":
                    board[x][y] = "X"
                if board[x][y] == "#":
                    board[x][y] = "O"


