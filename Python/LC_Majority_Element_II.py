class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return([])
    
        count_1,count_2,candidate_1,candidate_2 = 0,0,0,1
        for i in nums:
            if(i==candidate_1):
                count_1+=1
            elif(i==candidate_2):
                count_2+=1
            elif(count_1==0):
                candidate_1,count_1 = i,1
            elif(count_2==0):
                candidate_2,count_2 = i,1
            else:
                count_1-=1
                count_2-=1
        
        return [n for n in (candidate_1, candidate_2)
                    if nums.count(n) > len(nums) // 3]
        
        
