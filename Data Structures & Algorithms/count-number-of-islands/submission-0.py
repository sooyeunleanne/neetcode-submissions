class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(grid, r, c, visited):
            visited[r][c] = True

            dr = [-1, 0, 0, 1]
            dc = [0, -1, 1, 0]

            for i in range(4):
                new_r = r + dr[i]
                new_c = c + dc[i]

                if (0 <= new_r < rows
                    and 0 <= new_c < cols
                    and grid[new_r][new_c] == '1'
                    and not visited[new_r][new_c]):
                    dfs(grid, new_r, new_c, visited)
    
        islands = 0
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(grid, r, c, visited)
                    islands += 1
        
        return islands
            
                
