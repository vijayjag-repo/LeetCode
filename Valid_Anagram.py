class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a = collections.Counter(s)
        b = collections.Counter(t)
        if(a==b):
            return(True)
        else:
            return(False)
