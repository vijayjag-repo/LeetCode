class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left = 0
        right = 0
        ans = []
        idx = 0
        for i in range(len(s)):
            if(s[i]=='L'):
                left+=1
            elif(s[i]=='R'):
                right+=1
            
            if(left==right):
                ans.append(s[idx:i+1])
                idx = i+1
                left = 0
                right = 0
        
        return len(ans)
