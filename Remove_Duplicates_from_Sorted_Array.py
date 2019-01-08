
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = []
        for i in nums:
            if i not in new:
                new.append(i)
        
        for i in range(len(new)):
            nums[i] = new[i]
        
        return(len(new))
