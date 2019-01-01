class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        
        s = "leetcode"
        return 0.

        s = "loveleetcode",
        return 2.
        """  
        count_char = collections.Counter(s)
        for i,char in enumerate(s):
            if(count_char[char]==1):
                return(i)
        return(-1)
        
        
        
        
