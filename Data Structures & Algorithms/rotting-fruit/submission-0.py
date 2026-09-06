class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        fresh = 0 # count the number of fresh oranges and only increment time when you're actually processing a layer that causes new oranges to rot

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def findAdjFruits(r, c):
            nonlocal fresh
            
            for i in range(4):
                new_r = r + dr[i]
                new_c = c + dc[i]

                if (0 <= new_r < rows
                    and 0 <= new_c < cols
                    and grid[new_r][new_c] == 1):
                    grid[new_r][new_c] = 2 # rot the fresh fruit
                    fresh -= 1
                    queue.append((new_r, new_c))

        # queue the adjacent cells to rotten bananas
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2: # if you find a rotten banana
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        while queue and fresh > 0:
            for _ in range(len(queue)): # process all queue items at once (for one BFS layer)
                r, c = queue.popleft()
                findAdjFruits(r, c)
            
            time += 1
        
        return time if fresh == 0 else -1
