class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str  
        Approach:
        First, use zip to consider the array of strings as a matrix and find the transpose.
        Then, we just compare. If the first character doesnt match, then we return(""). Else, we go on comparing.
        Then we return the prefix.
        
        """
        prefix = ""
        
        new = zip(*strs)
        for i in new:
            for j in range(len(i)):
                if(i[0]!=i[j]):
                    if(new.index(i)==0):
                        return("")
                    else:
                        break
            if(j==len(i)-1 and i[0]==i[j]) :
                prefix+=i[0]
            
        return(prefix)
            
                
                
                
