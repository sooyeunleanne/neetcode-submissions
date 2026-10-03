class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        def dfs(r, c, visit, prevHeight):
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visit or
                heights[r][c] < prevHeight
            ):
                return
            
            prevHeight = heights[r][c]
            visit.add((r, c))

            for i in range(4):
                dfs(r + dr[i], c + dc[i], visit, prevHeight)
        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
