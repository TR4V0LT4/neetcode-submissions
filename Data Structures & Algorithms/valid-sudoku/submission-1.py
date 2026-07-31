from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #vertical check
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        

        #horizontal check
        
        for row in board:
            seen = set ()
            for value in row:
                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)
        #squarecheck

        for square_row in range(0,9,3):
            for square_col in range(0,9,3):
                square = set()
                for row in range(square_row,square_row+3):
                    for col in range(square_col,square_col+3):
                        value = board[row][col]
                        if value == '.':
                            continue
                        if value in square:
                            return False
                        square.add(value)
        return True