class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string = str(x)
        if(string[::-1] == str(x)):
            return(True)
        return(False)
        
