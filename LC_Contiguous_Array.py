class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Approach:
        
        Have a count value and update it on each occurence of 0 or 1.
        If you have the same count valut at say for index 2 and index 6, it means that there are equal number of 0's and 1's.
        Store the index information in a dict and calculate the maximum length possible.
        
        """
        d = dict()
        count = 0
        max_length = 0
        d[0] = -1
        
        for i in range(len(nums)):
            if(nums[i]==0):
                count-=1
            else:
                count+=1
                
            if(count in d):
                max_length = max(max_length,i-d[count])
            else:
                d[count] = i
        
        return(max_length)
