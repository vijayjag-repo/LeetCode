class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        Approach:
        Find the index of the zero present in the matrix. From this, we know which row and column we've to
        change into 0's. Iterate and set the corresponding row and column to 0.
        """
        new = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j]==0):
                    new.append((i,j))

        for value in new:
            row = value[0]
            column = value[1]
            for i in range(len(matrix[i])):
                matrix[row][i] = 0
            
            for i in range(len(matrix)):
                matrix[i][column] = 0
                
        
                    
                    
                
        
        
