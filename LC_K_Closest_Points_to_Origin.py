class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        # Solution 1:
        heap = []
        
        for (x, y) in points:
            #dist is negative because, heapq executes min heap. So, if you pop, you pop the smallest out of the heap, but the 
            #smallest one is the one with least euclidean dist. 
            #You dont want to remove that. So, you implement max heap by multiplying with -ve sign.
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return([(x,y) for (dist,x, y) in heap])
    
        # Solution 2:
        
        # same concept but just that you're storing all the values and then sorting them to get the K closest ones
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

    
            
        
        
        
        
