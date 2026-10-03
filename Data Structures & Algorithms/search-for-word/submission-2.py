class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False] * COLS for _ in range(ROWS)]

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or r >= ROWS or c < 0 or c >= COLS
                    or visited[r][c] or board[r][c] != word[i]):
                return False

            visited[r][c] = True
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))
            visited[r][c] = False

            return found

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False

        


            


        