class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        #20 - https://leetcode.com/problems/valid-parentheses/
        
        Optimal approach
        ------
        * Initialize a hashmap with the different pairs (so that we can lookup in O(1)) and also a stack
        * Run a loop through the input string
            * For each element that's in the hashmap, add to stack
            * For each element that's not in the hashmap, we need to check whether this element is the correct pair for the top most element (pop the stack to check)
                * If this is not the correct pair, then return False
                * Also, the stack will only be empty when all elements are done or no elements have been processed
                * If the stack is empty midway, then return False
                * ^Both these conditions can be clubbed together using OR
        
        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack = []
        pairs = {'{':'}','[':']','(':')'}
        
        for char in s:
            if (char in pairs):
                stack.append(char)
            elif (len(stack) == 0 or char != pairs[stack.pop()]):
                return False
        
        return len(stack) == 0
                    
                
        
