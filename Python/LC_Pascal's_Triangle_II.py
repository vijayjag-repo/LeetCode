class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = [[1]*(i+1) for i in range(rowIndex+1)]
        
        for i in range(rowIndex+1):
            for j in range(1,i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        return(triangle[rowIndex])
