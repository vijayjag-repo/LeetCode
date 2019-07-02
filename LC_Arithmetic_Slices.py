class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        
        Approach:
        Straightforward. If the difference between consecutive numbers is the same, increase count. 
        Else, make count 0 and continue. This count is the consecutive numbers count. 
        Also, have a total count to count the total number of arithmetic slices.
        
        """
        curr = 0
        total = 0
        for i in range(2,len(A)):
            if(A[i]-A[i-1]==A[i-1]-A[i-2]):
                curr+=1
                total+=curr
            else:
                curr = 0
        return(total)
        
