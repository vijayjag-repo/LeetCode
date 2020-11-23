class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        
        Approach:
        
        Sort the points based on the difference.
        The points favour city A in the beginning and as we progress, city B is favoured.
        So, for the first half points, we choose cityA and for the next, we choose cityB.
        
        """
        if not costs:
            return(0)
        
        costs.sort(key = lambda x:x[0]-x[1])
        ans = 0
        mid = len(costs)/2
        
        for i in range(len(costs)):
            if(i<mid):
                ans+=costs[i][0]
            else:
                ans+=costs[i][1]
        return(ans)
