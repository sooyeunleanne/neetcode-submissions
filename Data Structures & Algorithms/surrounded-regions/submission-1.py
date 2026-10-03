class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # start from "O"s on the edges, dfs them, mark those as not turnable
        # otherwise all the other "O"s can be replaced

        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c):
            if (
                0 <= r < ROWS and
                0 <= c < COLS and
                board[r][c] == "O"
            ):
                board[r][c] = "T" # don't flip

                dr = [-1, 1, 0, 0]
                dc = [0, 0, -1, 1]

                for i in range(4):
                    dfs(r + dr[i], c + dc[i])
            else:
                return
            
            
        for r in range(ROWS):
            dfs(r, 0)
            dfs(r, COLS - 1)
        
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = 'O'
                    
        
        return