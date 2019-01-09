class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Approach:
        Use counter to find the number of occurences of each number so as to append duplicate values.
        count is used to append as many duplicates present for a given number.
        Then sort and return the K-th largest.
        """    
        numbers = []
        new = collections.Counter(nums)
        print(new)
        for i in new:
            count = new[i]
            while(count>1):
                numbers.append(i)
                count-=1
            numbers.append(i)
        numbers.sort()    
        return(numbers[-k])    
        
