class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        
        Approach:
        
        First build the triangle. Using list comprehension this is pretty simple. 
        Then, you just have to iterate and update the values using the previous values.
       
        """
        triangle = [[1]*(i+1) for i in range(numRows)]
        
        for i in range(numRows):
            for j in range(1,i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        return(triangle)
