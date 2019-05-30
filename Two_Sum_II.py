class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers)-1
        sums = 0
        while(i<j):
            if(sums==target):
                return(i+1,j+1)
            elif(sums<target):
                i+=1
            elif(sums>target):
                j-=1
        
 
