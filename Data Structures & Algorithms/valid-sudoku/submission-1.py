class Solution:
    def isValidSudoku(self, board: list[str]) -> bool:
        row = collections.defaultdict(list)
        col = collections.defaultdict(list)
        square = collections.defaultdict(list)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                else:
                    if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3,c//3)]:
                        return False
                    row[r].append(board[r][c])
                    col[c].append(board[r][c])
                    square[(r//3,c//3)].append(board[r][c])
        return True