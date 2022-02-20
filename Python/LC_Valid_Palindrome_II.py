class Solution(object):  
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        
        https://leetcode.com/problems/valid-palindrome-ii/
        
        Given a string s, return true if the s can be palindrome after deleting at most one character from it.
        
        Example 1:
        Input: s = "aba"
        Output: true

        Example 2:
        Input: s = "abca"
        Output: true
        Explanation: You could delete the character 'c'.
        
        Example 3:
        Input: s = "abc"
        Output: false
        """
        
        def isPalindrome(s):
            if (s == s[::-1]):
                return True
            return False
        
        if (len(s) == 0):
            return True
        
        left = 0
        right = len(s) - 1
        
        while(left <= right):
            if (s[left] != s[right]):
                left_s = s[:left] + s[left+1:]
                right_s = s[:right] + s[right+1:]
                return isPalindrome(left_s) or isPalindrome(right_s)
            else:
                left += 1
                right -= 1
                
        return True
                    
