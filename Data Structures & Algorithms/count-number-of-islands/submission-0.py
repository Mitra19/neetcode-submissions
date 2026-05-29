class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, r, c,visit):
            ROW, COL = len(grid), len(grid[0])
            if min(r,c) < 0 or r == ROW or c == COL or (r,c) in visit or grid[r][c] == "0":
                return
            visit.add((r,c))
            if grid[r][c] == "1" and r >= 0 and c >= 0 and r < ROW and c < COL:
                dfs(grid, r, c+ 1, visit)
                dfs(grid, r, c-1, visit)
                dfs(grid, r+1, c,visit)
                dfs(grid, r-1,c, visit)
        visit = set()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i,j) not in visit:
                    dfs(grid, i,j,visit)
                    ans+=1
        return ans

