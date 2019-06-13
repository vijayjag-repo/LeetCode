class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewel_collection = collections.Counter(S)
        count = 0
        for i in J:
            count+=jewel_collection[i]
        
        return(count)
