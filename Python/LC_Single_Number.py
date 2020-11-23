class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Approach 1 : Bit Manipulation
        # XOR all the numbers. The duplicate numbers will be zero. 
        # a ^ 0 = a, a ^ a = 0.
        # Single number will be XOR-ed with zero to get the number itself.
        # Time and space = O(N) and O(1)
        
        a = 0
        for i in nums:
            a ^=i
        return(a)
    
    ----------------------------------------------------
    ----------------------------------------------------
        # Approach 2: Dictionary. Self Explanatory.
        # Time and space = O(N) and O(N)
        d = dict()
            for i in nums:
                if i not in d:
                    d[i] = 1
                else:
                    del d[i]

            for i in d:
                return(i)
                
        
