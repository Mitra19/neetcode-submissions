class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        def dfs(grid, r, c, visit):
            ROW, COL = len(grid), len(grid[0])
            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] == "X" or (r,c) in visit:
                return
            visit.add((r,c))
            if grid[r][c] == "O":
                grid[r][c] = "T"
            dfs(grid, r, c+1, visit)
            dfs(grid,r, c-1, visit)
            dfs(grid, r+1, c, visit)
            dfs(grid, r-1, c, visit)
        visit = set()
        for i in range(len(grid[0])):
            if grid[0][i] == "O":
                dfs(grid,0,i, visit)
            if grid[len(grid)-1][i] == "O":
                dfs(grid, len(grid)-1, i, visit)
        for j in range(len(grid)):
            if grid[j][0] == "O":
                dfs(grid,j, 0 , visit)
            if grid[j][len(grid[0])-1] == "O":
                dfs(grid, j, len(grid[0])-1, visit)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "O":
                    grid[i][j] = "X"
                if grid[i][j] == "T":
                    grid[i][j] = "O"
        return grid 
        