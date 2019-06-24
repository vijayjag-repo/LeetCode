class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # Solution 1
        a = ""
        b = ""
        
        for i in S:
            if(i!='#'):
                a+=i
            else:
                a = a[:-1]
        for i in T:
            if(i!='#'):
                b+=i
            else:
                b = b[:-1]
        return(a==b)
        
        -------------------------------------------------------------------------
        -------------------------------------------------------------------------
        # Solution 2 using stack
        class Solution(object):
            def backspaceCompare(self, S, T):
                """
                :type S: str
                :type T: str
                :rtype: bool
                """

                stack_s = []
                stack_t = []

                for i in S:
                    if(len(stack_s)>0 and i=='#'):
                        stack_s.pop()
                    if(i!='#'):
                        stack_s.append(i)

                for i in T:
                    if(len(stack_t)>0 and i=='#'):
                        stack_t.pop()
                    if(i!='#'):
                        stack_t.append(i)

                return(stack_s==stack_t)
                
        
        
        
            
        
