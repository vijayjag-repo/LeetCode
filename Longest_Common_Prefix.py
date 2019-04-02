class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str  
        Approach:
        First, use zip to consider the array of strings as a matrix and find the transpose.
        Now, run two for-loops and compare if each element in the tuple is the same.
        If same, add it to the prefix.
        Moreover, since the question is about prefix, we need to check if the first tuple has all same elements. 
        If not, we can return an empty string because the first character of all the strings in the array must be the same.
        
        """
        prefix = ""
        value = 0
        new = zip(*strs)
        for i in new:
            value+=1
            count = 0
            for j in range(len(i)):
                if(i[j]==i[0]):
                    count+=1
                if(count==len(i)):
                    prefix+=i[0]
            if(value==1 and count<len(i)):
                return("")
      
        return(prefix)
            
                
                
                
