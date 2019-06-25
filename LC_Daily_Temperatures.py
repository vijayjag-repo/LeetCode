class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        
        Approach:
        Use the classical stack method. 
        Push elements onto the stack and keep doing until you have an element greater than the stack[top].
        If element > stack[top], keep popping until you cannot.
        Whenever you pop, append the difference in the index of the popped element and the current element.
        Finally, return the answer. 
        
        One catch that I faced. I inserted the elements onto the stack and found out index using T.index(stack[-1]).
        However, if you are having duplicate elements, this method would fail.
        Instead, append the indexes on the elements onto the stack and then compare incoming element with this T[stack[-1]].
        
        """
        stack = []
        ans = [0]*len(T)
        
        for i in range(len(T)):
            while(len(stack)>0):
                if(T[i]>T[stack[-1]]):
                    ans[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    break
            stack.append(i)
        
        return(ans)
            
