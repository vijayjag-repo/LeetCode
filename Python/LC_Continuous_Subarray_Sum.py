class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        
        Approach:
        Same as Subarray sum equals K with modification.
        Basic idea is that, 
        If you get the same remainder again, it means that you've encountered some sum which is a multiple of K.

        Example:
        nums = [23,2,4], k = 6
        Lets, walk through the code with the example. 
        (i=0) : sums = 23 => 23%6 => (sums = 5)
        (i=1) : sums = 5+2=7 => 7%6 => (sums = 1)
        (i=2) : sums = 1+4=5 => 5%6 => (sums = 5)

        We've encountered the same sums(remainder) again. So we have found the subarray. But, there's
        another aspect to this problem. The subarray must have a minimum size of 2. 
        That is why we check if (i - d[sums])>1. 
        In the above example, this if loop is executed when (i=2) and (d[sums]=1). 
        In other words, the same remainder(sums=5) has been encountered twice and then we check for the respective difference in indices.

        Counter example to understand this. Let's take nums = [23,6], k = 6
        (i=0) : sums = 23 => 23%6 => (sums = 5)
        (i=1) : sums = 5+6=11 => 11%6 => (sums = 5)

        So, the same sums(remainder) has appeared again which means we've found the subarray but it is not a subarray of size 2 or more.
        Because they've occurred next to each other, which means that, we have just one element in the subarray which contributes.
        If you remove 23 from the nums array and keep 6 alone, it will still be a subarray whose sum%k is 0. 
        This is the reason why we calculate the index difference and then return True.
           
          
        """
        d = dict()
        d[0] = -1
        sums = 0
        
        for i in range(len(nums)):
            sums+=nums[i]
            if(k!=0):
                sums = sums%k
            if(sums in d):
                if(i-d[sums]>1):
                    return(True)
            else:
                d[sums] = i
        
        return(False)
