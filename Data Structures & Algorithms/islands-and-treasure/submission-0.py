class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0: # queue treasure chests
                    queue.append((r, c))
        
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        while queue:
            r, c = queue.popleft()

            for i in range(4):
                new_r = r + dr[i]
                new_c = c + dc[i]
                
                if (0 <= new_r < rows
                and 0 <= new_c < cols
                and grid[new_r][new_c] == 2147483647):
                    grid[new_r][new_c] = 1 + grid[r][c]
                    queue.append((new_r, new_c))
            