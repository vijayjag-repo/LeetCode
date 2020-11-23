class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        
        Approach:
        
        Expand around center
        Same as Longest Palindromic Substring. Except that, whenever you find a valid palindromic substring, you append to ans.
        Whereas in Longest Palindromic Substring, you append only when you hit the longest. ie: you return only when the while loop fails.
        """
        if not s:
            return 0
        
        ans = []
        def helper(beg,end,s):
            while(beg>=0 and end<len(s) and s[beg]==s[end]):
                beg-=1
                end+=1
                if(len(s[beg+1:end])>0):
                    ans.append(s[beg+1:end])
                
        for i in range(len(s)):
            helper(i,i,s)
            helper(i,i+1,s)
            
        return len(ans)
        
