class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        
        Approach:
        Basic idea is that in a palindrome, each character if present twice if length=even and similarly for odd except one char.
        So, we just add the count of the character and if its odd, you add the count-1. 
        Finally, we add +1 if some character is present odd number of times because atmost one character can be present odd number of times.
        
        """
        flag = False
        ans = 0
        count = collections.Counter(s)
        
        for i in count:
            if(count[i]%2==0):
                ans+=count[i]
            else:
                flag = True
                ans+=count[i]-1
        
        if(flag):
            ans+=1
        return(ans)
