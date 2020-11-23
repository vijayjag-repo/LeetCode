class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = []
        opened = 0
        
        for item in S:
            if(item=='(' and opened>0):
                ans.append(item)                
            if(item==')' and opened>1):
                ans.append(item)
            
            if(item=='('):
                opened+=1
            else:
                opened-=1
        return("".join(ans))
