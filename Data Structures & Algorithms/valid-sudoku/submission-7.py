class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        cols = [[] for _ in range(9)]
        boxes = [[] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue

                if num in rows[r]:
                    return False
                
                rows[r].append(num)

                if num in cols[c]:
                    return False
                cols[c].append(num)

                b = (r // 3) * 3 + (c // 3)
                if num in boxes[b]:
                    return False
                boxes[b].append(board[r][c])

        return True
