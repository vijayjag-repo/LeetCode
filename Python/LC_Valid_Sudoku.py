class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
        Approach:
        
        First check for the row validity and then check for column validity and then check for square validity.
        """
        def row_valid(board):
            for row in board:
                if not unit_valid(row):
                    return False
            return True
        
        def col_valid(board):
            for col in zip(*board):
                if not unit_valid(col):
                    return False
            return True
        
        def square_valid(board):
            for i in (0,3,6):
                for j in (0,3,6):
                    square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                    if not unit_valid(square):
                        return False
            return True
            
        def unit_valid(unit):
            val = [i for i in unit if i!='.']
            return len(set(val))==len(val)
            
        return row_valid(board) and col_valid(board) and square_valid(board)
        
