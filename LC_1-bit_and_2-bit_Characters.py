class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        ans = True
        while(i<len(bits)):
            if(bits[i]==0):
                ans = True
                i+=1
            elif(bits[i]==1 and (bits[i+1]==0 or bits[i+1]==1)):
                ans = False
                i+=2
        return(ans)
            
