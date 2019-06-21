class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Solution 1
        if(len(s)!=len(t)):
            return(False)
        d = dict()
        for i in s:
            if(i not in d):
                d[i] = 1
            else:
                d[i]+=1
        
        for i in t:
            if(i in d):
                d[i]-=1
                if(d[i]<0):
                    return(False)
            else:
                return(False)
        return(True)
        _________________________________________________________
        # Solution 2
        a = collections.Counter(s)
        b = collections.Counter(t)
        if(a==b):
            return(True)
        else:
            return(False)
