class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        
        Approach:
        
        Clever usage of space. Just append the number of people at respective timestamps. If at any point,
        the number of people go beyond capacity, you've to return False.
        """
        if not trips:
            return(True)
        
        stops = [0]*1000
        
        for x in trips:
            stops[x[1]]+=x[0]
            stops[x[2]]-=x[0]
        
        total = 0
        for i in range(len(stops)):
            total+=stops[i]
            if(total>capacity):
                return(False)
        return(True)
