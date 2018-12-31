class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        a = []
        for i in nums:
            if(count>=0):
                if i not in a:
                    a.append(i)
                else:
                    a.remove(i)
                    count = 1
        return(a[0])
        
