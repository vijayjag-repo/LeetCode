class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        
        Approach:
        
        Same as valid parentheses.
        """
        if not S:
            return("")
        stack = []
        for item in S:
            if(stack and item==stack[-1]):
                stack.pop()
            else:
                stack.append(item)
        
        return("".join(stack))
