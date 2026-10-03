class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while queue:
            r, c = queue.popleft()

            for i in range(4):
                new_r, new_c = r + dr[i], c + dc[i]

                if (0 <= new_r < ROWS and
                    0 <= new_c < COLS and
                    grid[new_r][new_c] == 2147483647):
                    grid[new_r][new_c] = 1 + grid[r][c]
                    queue.append((new_r, new_c))
        
        return
