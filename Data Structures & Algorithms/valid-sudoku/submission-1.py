class Solution:
    def get_col(self, board: List[List[str]], idx: int) -> list[str]:
        col = []
        for r in board:
            if r[idx] != ".":
                col.append(r[idx])
        return col
    def get_row(self, board: List[List[str]], idx: int) -> list[str]:
        row = []
        for r in board[idx]:
            if r != ".":
                row.append(r)
        return row
    def get_flat_square(self, board: List[List[str]], box: int) -> list[str]:
        box_row = (box // 3) * 3
        box_col = (box % 3) * 3
        flat_square = []
        for row in board[box_row:box_row+3]:
            for cell in row[box_col:box_col+3]:
                if cell != ".":
                    flat_square.append(cell)
        return flat_square
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            square = self.get_flat_square(board, i)
            if len(square) != len(set(square)):
                return False
            row = self.get_row(board, i)
            if len(row) != len(set(row)):
                return False
            col = self.get_col(board, i)
            if len(col) != len(set(col)):
                return False
        return True
   