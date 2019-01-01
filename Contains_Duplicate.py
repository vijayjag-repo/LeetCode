class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        
        Approach :
            We get the number of occurences of each element in the array. If count greater than 1, return True
        
        """
        n = collections.Counter(nums)
        print(n)
        for i,value in enumerate(nums):
            if(n[value]>1):
                return(True)
        return(False)
            
