class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(board, r, c, visit):
            ROW, COL = len(board), len(board[0])
            if min(r,c) < 0 or r == ROW or c == COL or board[r][c] == "X" or (r,c) in visit:
                return
            visit.add((r,c))
            if board[r][c] == "O":
                board[r][c] = "T"
            dfs(board, r, c+1, visit)
            dfs(board,r, c-1, visit)
            dfs(board, r+1, c, visit)
            dfs(board, r-1, c, visit)
        visit = set()
        for i in range(len(board[0])):
            if board[0][i] == "O":
                dfs(board,0,i, visit)
            if board[len(board)-1][i] == "O":
                dfs(board, len(board)-1, i, visit)
        for j in range(len(board)):
            if board[j][0] == "O":
                dfs(board,j, 0 , visit)
            if board[j][len(board[0])-1] == "O":
                dfs(board, j, len(board[0])-1, visit)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "T":
                    board[i][j] = "O"
        return