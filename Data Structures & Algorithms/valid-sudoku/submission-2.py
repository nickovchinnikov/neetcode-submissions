class Solution:
    def check_col(self, board: List[List[str]], idx: int) -> bool:
        seen = set()
        for row in board:
            x = row[idx]
            if row[idx] == ".":
                continue
            if x in seen:
                return False
            seen.add(x)
        return True
    def check_row(self, board: List[List[str]], idx: int) -> bool:
        seen = set()
        for x in board[idx]:
            if x == ".":
                continue
            if x in seen:
                return False
            seen.add(x)
        return True
    def check_square(self, board: List[List[str]], box: int) -> list[str]:
        box_row = (box // 3) * 3
        box_col = (box % 3) * 3
        seen = set()
        for row in board[box_row:box_row+3]:
            for cell in row[box_col:box_col+3]:
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            is_square = self.check_square(board, i)
            is_row = self.check_row(board, i)
            is_col = self.check_col(board, i)
            if is_square and is_row and is_col:
                continue
            return False
        return True
   