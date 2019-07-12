class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        
        Approach:
        If entering element is same as top, remove from stack. Else, keep adding. 
        """
        i = 0
        stack = []
        while(i<len(S)):
            if(not stack or S[i]!=stack[-1]):
                stack.append(S[i])
            else:
                stack.pop()
            i+=1
        
        return("".join(stack))
                
                
       
        
                
