class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(num)):
            while stack and k > 0:
                if num[i] < stack[-1]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[i])
        
        #To check for remaining k digits. If present, remove them.
        while(k != 0):
            stack.pop()
            k -= 1
        
        #Remove leading zeroes.
        while(stack):
            if stack[0] == '0':
                stack = stack[1:]
            else:
                break
        
        return(''.join(stack) or '0')
