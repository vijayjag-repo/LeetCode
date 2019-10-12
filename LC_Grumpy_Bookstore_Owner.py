class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
 
        """
        minval = [customers[i] for i in range(len(customers)) if grumpy[i]==0]
        maxval = 0
        temp = 0

        for i in range(len(customers)):
            if(i<X):
                if(grumpy[i]==1):
                    temp+=customers[i]
            else:
                if(grumpy[i]==1):
                    temp+=customers[i]
                if(grumpy[i-X]==1):
                    temp-=customers[i-X]
                    
            maxval = max(maxval,temp)
        
        return sum(minval)+maxval
            
                
        
        
