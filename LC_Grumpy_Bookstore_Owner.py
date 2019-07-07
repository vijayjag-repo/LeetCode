class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        
        Approach:
        1) First, you count the satisfied customers and set satisifed customers index to 0.
        2) Now, you just have to count the max sum of window of length X.
        """

        i = 0
        base = 0
        sums = 0
        prev_sums = 0
        
        for i in range(len(grumpy)):
            if(grumpy[i]==0):
                base+=customers[i]
                customers[i]=0
        
        i = 0
        for i in range(len(customers)):
            if(i<X):
                prev_sums+=customers[i]
                sums = prev_sums
            else:
                prev_sums = prev_sums + customers[i] - customers[i-X]
                sums = max(sums,prev_sums)
                
        return(sums+base)
            
                
        
