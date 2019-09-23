class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        
        Approach:
        
        Put everything onto stack
        Since its preorder, if an element is lesser than previous, then we're still in the left subtree.
        If an element is greater than previous, we have moved to right subtree of ancestor/parent. 
        Now low must be updated to parent/ancestor value using repeated pop() operations.
        
        If at any point, the incoming value is less than low value, we know it's not pre order.
        
        """
        stack = []
        low = float('-inf')
        for p in preorder:
            if(p<low):
                return(False)
            while(stack and p>stack[-1]):
                low = stack.pop()
            stack.append(p)
        return(True)
