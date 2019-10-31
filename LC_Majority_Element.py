class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        count = collections.Counter(nums)
        for i,value in enumerate(nums):
            if(count[value]>length/2):
                return(value)
            
# Boyer-Moore Voting
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Approach:
        
        Main idea is that, if an element is present more than 1/2 of the length of the array, then its score would be larger.
        Even if other elements try to cancel out by -1, you'll still end up with the score >0.
        If and only if you end up with a count>0, you know there's a candidate(majority element).
        
        """
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count+= 1 if num==candidate else -1
        
        return candidate
        
        
