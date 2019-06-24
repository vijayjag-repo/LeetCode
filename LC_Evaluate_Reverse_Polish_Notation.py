class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        Approach:
        
        If you see an element not in operators, you just append it because its a number.
        But, if you see an operator, then, you need to evaluate the answer for the last two operands inserted into the stack.
        So, pop the two elements and perform the operation and put it back onto the stack.
        At the end, you'll be ending up with only one element in the stack which is the final answer.
        """
        stack = []
        operators = ["*","+","-","/"]
        
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                r = stack.pop()
                l = stack.pop()
                
                if(i == "+"):
                    stack.append(l+r)
                elif(i == "-"):
                    stack.append(l-r)
                elif(i == "*"):
                    stack.append(l*r)
                else:
                    stack.append(int(float(l)/r))
        return(stack.pop())
