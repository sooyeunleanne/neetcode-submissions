class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def dfs(r, c):
            if (r < 0 or r >= ROWS
                or c < 0 or c >= COLS
                or visited[r][c]
                or grid[r][c] == "0"):
                return
            
            visited[r][c] = True

            for i in range(4):
                dfs(r + dr[i], c + dc[i])
        
        n = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and not visited[r][c]:
                    n += 1
                    dfs(r, c)
        
        return n


