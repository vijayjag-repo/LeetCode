class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        Example 1:

        Input: 00000000000000000000000000001011
        Output: 3
        Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
        Example 2:

        Input: 00000000000000000000000010000000
        Output: 1
        Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
        
        """
        count = 0
        mask = 1
        for i in range(0,32):
            if(n&mask!=0):
                count+=1
            mask = mask<<1
        return(count)
        