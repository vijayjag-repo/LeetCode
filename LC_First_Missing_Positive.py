class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Approach:
        Since we've to return the least missing positive number, we just scan for numbers from 1-infinity
        If,
          1 is not present, we return 1
        Else,
          we check if 2 is present or not. Else, we check for 3 and so on.
        """
        if not nums:
            return(1)
        i = 1
        while(i>0):
            if(i not in nums):
                return(i)
            else:
                i+=1
