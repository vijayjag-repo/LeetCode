class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        
        Straightforward. If you are starting new on stacks,
        this is one of the easier questions to start off with. 
        """
        stack = []
        
        for i in range(len(ops)):
            if(ops[i]=='C'):
                stack.pop()
            elif(ops[i]=='D'):
                stack.append(2*stack[-1])
            elif(ops[i]=='+'):
                stack.append(stack[-1]+stack[-2]) 
            else:
                stack.append(int(ops[i]))
            
        return(sum(stack))
