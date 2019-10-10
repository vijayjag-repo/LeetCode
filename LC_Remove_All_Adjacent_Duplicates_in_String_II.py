class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        
        Approach:
        
        Nice use of sets to deal with adjacent elements that are same.
        TLE though. Shorter version compared to other approach.
        """
        if not s:
            return ""
        if(k>len(s)):
            return ""
        
        i = 0
        j = k-1
        
        while(len(s[i:j+1])>=k):
            if(len(set(s[i:j+1]))==1):
                s = s[:i] + s[j+1:]
                i = 0
                j = k-1
            else:
                i+=1
                j+=1
        
        return s
            
class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        
        Approach:
        
        Uses stack to check 
        """
        if not s:
            return ""
        if(k>len(s)):
            return ""
        stack = [s[0]]
        
        count = 0
        for char in s[1:]:
            stack.append(char)
            while(len(stack)>=k):
                # print('Initial',stack)
                for val in stack[-k:]:
                    if(val==stack[-1]):
                        count+=1
                # print("Count here",count)
                if(count==k):
                    # print("Hello")
                    for i in range(k):
                        stack.pop()
                    count = 0
                    break
                else:
                    count = 0
                    break
        
        return "".join(stack)
           
            
        
        
                
                    
                
