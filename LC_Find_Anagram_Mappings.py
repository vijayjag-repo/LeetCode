class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        index_B = dict()
        ans = []
        
        for i in range(len(B)):
            index_B[B[i]] = i
        
        return([index_B[i] for i in A])
