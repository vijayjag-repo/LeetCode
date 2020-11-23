class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        
        Approach:
        
        Classic Stack. Similar to Decode String problem.
        """
        stack = [[]]
        
        for char in s:
            if(char=='('):
                stack.append([])
            elif(char==')'):
                temp = stack.pop()[::-1]
                stack[-1]+=temp
            else:
                stack[-1]+=char
        
        return("".join(stack[-1]))
        
        
