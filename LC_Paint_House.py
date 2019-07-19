class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        
        Approach:
        
        Stefan Pochmann, the God!
        Pretty simple approach and good use of list comprehension.
        Here, we have only 3 colours. Also, we need to minimize the cost amap.
        Two adjacent houses cannot have the same colour.
        
        At every single row in the matrix, we calculate the min possible cost.
        Say our matrix is: [17,2,17]
                           [16,16,5]
                           
        In the first iteration, our row is and we get our prev = [17,2,17]
        Second iteration, we have our row to be [16,16,5] and the prev = current value + min(previous values except the current index)
        i.e: we get prev = [16+min(2,17),16+min(17,17), 5+min(17,2). We essentially omit the current index from the previous row while calcuating min.
        """
        prev = [0]*3
        
        for curr in costs:
            prev = [curr[i] + min(prev[:i]+prev[i+1:]) for i in range(3)]
        
        return(min(prev))
