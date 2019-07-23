# Clean Solution
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        All you need is the shortest string and the longest string.
        """
        if(len(strs)==0):
            return("")
        
        shortest = min(strs)
        longest = max(strs)
        
        for index,val in enumerate(shortest):
            if(val!=longest[index]):
                return(shortest[:index])
        return(shortest)
    
# Another approach
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        
        Approach:
        First get the shortest string in the list of strings.
        Then for each character in this short string, compare it with the corresponding character in the other strings.
        If same, keep going.
        Else, return the string until which the character matches.
        """
        if(len(strs)==0):
            return("")
        
        shortest = min(strs,key=len)
        
        for index,val in enumerate(shortest):
            for other in strs:
                if(other[index]!=val):
                    return(shortest[:index])
        return(shortest)
                
# Old solution using zip
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

                
                
