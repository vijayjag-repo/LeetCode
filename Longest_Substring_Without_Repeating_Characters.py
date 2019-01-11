class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = set()
        left,right,longest = 0,0,0
        while(left<len(s) and right<len(s)):
            if(s[right] not in chars):
                chars.add(s[right])
                right+=1
                longest = max(longest,right-left)
            else:
                chars.remove(s[left])
                left+=1
        return(longest)
        
