class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        Approach:
        First, reverse each row
        Second, Complement the value present
        Return the matrix
        """
        for i in range(len(A)):
            A[i] = A[i][::-1]
            for j in range(len(A[i])):
                A[i][j] = 1 - A[i][j]
        return(A)
                
                
            
        
        
