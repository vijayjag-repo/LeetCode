class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        
        Approach:
        
        Manipulate the matrix properties gives.
        Start from the bottom. 
        If the current value is greater than target, go up(You want a lesser value).
        If the current value is lesser than target, go right(You want a greater value).
        """
        if(len(matrix)==0):
            return(False)
        
        row,col = len(matrix),len(matrix[0])
        
        i = row - 1
        j = 0
        
        while(i>=0 and j<col):
            if(matrix[i][j]>target):
                i-=1
            elif(matrix[i][j]<target):
                j+=1
            else:
                return(True)
        return(False)
