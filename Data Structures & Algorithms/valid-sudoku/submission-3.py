class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(len(board)):
            for c in range(len(board)):
                val = board[r][c]

                if val == ".":
                    continue
                
                row = ("row", r, val)
                col = ("col", c, val)
                box = ("box", r // 3, c // 3, val)

                if row in seen or col in seen or box in seen:
                    return False
                
                seen.add(row)
                seen.add(col)
                seen.add(box)
                
        return True
        