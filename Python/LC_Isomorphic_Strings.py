class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Approach:
        We scan each word from both the string and copy it to a dictionary.
        As we scan, if there's a duplicate entry or link, then we return False
        """
        d1 = dict()
        d2 = dict()
        for i in range(len(s)):
            if(s[i] not in d1):
                d1[s[i]] = t[i]
            if(t[i] not in d2):
                d2[t[i]] = s[i]
            if(d1[s[i]]!=t[i] or d2[t[i]]!=s[i]):
                return(False)
        return(True)
        
        
        
