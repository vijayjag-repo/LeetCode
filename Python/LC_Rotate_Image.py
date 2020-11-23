class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix)
        for i in range(len(nums)):
            matrix[i] = matrix[i][::-1]
           
