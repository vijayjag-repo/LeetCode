class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        b = collections.Counter(S)
        for i in collections.Counter(J):
            if(i in b):
                count+= b[i]
        return(count)
        
