class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        
        Approach:
        Just sort the items and then find the sums and avg for each individual student without using extra space.
        """
        items.sort(reverse=True)
        ans = []
        sums = 0
        count = 0
        check = items[0][0]
        
        for ind,val in items:
            if(ind==check):
                if(count<5):
                    sums+=val
                    count+=1
            else:
                ans.append([check,sums/5])
                sums = val
                count = 1
                check = ind
    
        ans.append([check,sums/5])
        return(ans[::-1])
# Approach 2: Using priority queue
# Little slower
from collections import defaultdict
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = collections.defaultdict(list)
        
        for idx,val in items:
            heapq.heappush(queue[idx],val)
            
            if(len(queue[idx])>5):
                heapq.heappop(queue[idx])
        ans = [[i,sum(queue[i])/5] for i in queue]
        return(ans)
        
        
        
