class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s)-1
        while(l<r):
            while(l<r and not s[l].isalnum()):
                l+=1
            while(l<r and not s[r].isalnum()):
                r-=1
            if(s[l].lower()!=s[r].lower()):
                return(False)
            l+=1
            r-=1
        return(True)
# Without while loops
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Approach:
        
        Just avoid spaces and keep moving 
        """
        l = 0
        r = len(s)-1
        while(l<r):
            # if there's a space, you just move forward.
            if(not s[l].isalnum()):
                l+=1
            elif(not s[r].isalnum()):
                r-=1
            else:
                if(s[l].lower()!=s[r].lower()):
                    return(False)
                else:
                    l+=1
                    r-=1
        return(True)
