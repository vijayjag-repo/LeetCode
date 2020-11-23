class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        
        Approach:
        
        Straight forward.
        matrix[mid/col][mid%col] is just to get to the index of that element.
        
        Draw a simple matrix to get this.
        """
        if not matrix:
            return(False)
        
        rows,col = len(matrix),len(matrix[0])
        low, high = 0, rows*col - 1
        
        while(low<=high):
            mid = (low+high)/2
            num = matrix[mid/col][mid%col]
            if(num==target):
                return(True)
            elif(num<target):
                low = mid + 1
            else:
                high = mid - 1
        return(False)
                
