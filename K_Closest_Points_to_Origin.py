class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        minimum = abs((points[0][0]-0)**2 + (points[0][1]-0)**2)
        value = []
        final = []
        for i in range(len(points)):
            sums = abs((points[i][0]-0)**2 + (points[i][1]-0)**2)
            value.append([sums,[points[i][0],points[i][1]]])
        
        value.sort()
        count = 0
        while(count<K):
            final.append(value[count][1])
            count+=1
        
        return(final)

    
            
        
        
        
        
