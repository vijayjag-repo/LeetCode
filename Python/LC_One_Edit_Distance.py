class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Approach:
        1) You always want s to be of lower or equal length. If not, then just reverse it.
        2) If len(t)-len(s)>1, it means that the Edit distance is already more than 1. So just return False.
        3) Iterate through s, if s[i]!=t[i], 
           If the strings are of same length, we have reached an edit distance of 1 already.
           So, we just check if there are any more mismatches.
           If the strings are of different lengths, we have reached an edit distance of 1 already.
           So, we just check if there are any more mismatches.
        4) If we have reached the end of s and there are still some characters in t, we check for the number of
           characters remaining in t. If it is more than 1, then return False
        """
        if(len(s)>len(t)):
            return(self.isOneEditDistance(t,s))
        
        if(len(t)-len(s)>1):
            return(False)
        
        for i in range(len(s)):
            if(s[i]!=t[i]):
                if(len(s)==len(t)):
                    return(s[i+1:]==t[i+1:])
                else:
                    return(s[i:]==t[i+1:])
        
        return(len(s)+1==len(t))
            
            
