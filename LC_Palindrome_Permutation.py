class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        
        Approach:
        
        Store the counts in dict.
        If string has odd length, then all characters are present even number of times except the middle one.
        If string has even length, then all characters are present even number of times.
        Using this fact, just find the sum of the mod values.
        This sum is equal to 0 for even length and 1 for odd length.
        Using this, you can tell whether some permutation of a given string can be a palindrome or not.
        
        """
        d = dict()
        for i in range(len(s)):
            if(s[i] not in d):
                d[s[i]] = 1
            else:
                d[s[i]]+=1
        
        count = 0
        for i in d:
            count+=d[i]%2
        
        return(count<=1)
