class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                if grid[r][c] == 1:
                    fresh += 1
        
        dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
        elapsed = 0
        while queue:
            r, c, h = queue.popleft()
            elapsed = max(elapsed, h)

            for i in range(4):
                adj_r, adj_c = r + dr[i], c + dc[i]

                if (
                    0 <= adj_r < ROWS and 
                    0 <= adj_c < COLS and
                    grid[adj_r][adj_c] == 1
                ):
                    grid[adj_r][adj_c] = 2
                    fresh -= 1
                    queue.append((adj_r, adj_c, h + 1))
            
        return elapsed if fresh == 0 else -1
        