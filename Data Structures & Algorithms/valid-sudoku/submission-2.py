class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])

        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        for row in range(rows):
            for col in range(cols):
                d = board[row][col]

                if d == ".":
                    continue
                
                if d in row_set[row]:
                    return False
                else: 
                    row_set[row].add(d)
                
                if d in col_set[col]:
                    return False
                else:
                    col_set[col].add(d)

                box = (row // 3) * 3 + (col // 3)
                if d in box_set[box]:
                    return False
                else:
                    box_set[box].add(d)
        
        return True