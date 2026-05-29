from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        time, fresh = 0,0
        queue = deque()
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    queue.append((i,j))
                if grid[i][j] == 1:
                    fresh+=1
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                neighbour = [(0,1),(0,-1),(1,0),(-1,0)]
                for dr, dc in neighbour:
                    row, col = r+dr, c+dc
                    if (row < 0 or row >= ROW) or (col < 0 or col >= COL) or grid[row][col] == 0:
                        continue
                    if grid[row][col] == 1:
                        fresh-=1
                        grid[row][col] = 2
                        queue.append((row, col))
            time+=1
        print(f"time: {time} fresh: {fresh}")
        return time if fresh == 0 else -1