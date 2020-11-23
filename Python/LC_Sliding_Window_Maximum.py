from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        result = []
        
        for i in range(len(nums)):
            # the first/left (max) element is out of the current window
            if(q and i - q[0]==k):
                q.popleft()  
            while(q):
                # pop useles elements from last/right of the queue
                if(nums[q[-1]] < nums[i]):
                    q.pop()
                else:
                    break
            q.append(i)
            
            if(i >= k-1): # i == k-1 is the beginning of a full window
                result.append(nums[q[0]])
            
        return(result)

# Naive Approach

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return([])
        i = 0
        ans = []
        while(i<k and k<=len(nums)):
            ans.append(max(nums[i:k]))
            i+=1
            k+=1
        return(ans)
