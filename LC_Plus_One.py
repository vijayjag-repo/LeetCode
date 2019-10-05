class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        
        Approach:
        
        As long as the digit is 9, you have to make it 0.
        So you scan from the right, if you see a 9, you make it 0 and move left.
        If count==len(digits), you've encountered only 9's. So you add 1 to the left and then return the list.
        Otherwise, you just add 1 wherever, you don't encounter a 9.
        """
        if not digits:
            return []
        
        i = len(digits)-1
        count = 0
        while(digits[i]==9 and i>=0):
            count+=1
            digits[i] = 0
            i-=1
        
        if(count==len(digits)):
            return [1] + digits
        else:
            digits[i]+=1
            return digits
            
