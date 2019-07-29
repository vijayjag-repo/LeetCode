class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        
        Pochmann!!
        
        """
        ok = [True]
        for i in range(1,len(s)+1):
            if(any(ok[j] and s[j:i] in wordDict for j in range(i))):
                ok.append(True)
            else:
                ok.append(False)
        return(-1)
