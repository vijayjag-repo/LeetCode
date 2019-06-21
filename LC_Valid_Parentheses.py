class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pairs = {'{':'}','[':']','(':')'}
        
        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                if(len(stack)==0 or stack.pop()!=char):
                    return(False)
        
        if(len(stack)==0):
            return(True)
        else:
            return(False)
        
