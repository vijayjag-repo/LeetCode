class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        Approach:
        First, you append the first element of nums2 to the stack. 
        If the next/incoming element of nums2 is greater thant the stack[top] a.k.a last element inserted to the stack,
        then, d[stack.pop()] = this incoming element. And you keep doing this in a while loop until this holds true.
        Because, if this incoming element is greater than all the elements present in the stack, then,
        you need to return this element. 
        If an incoming element is lesser than the stack[top], just insert it to the stack and make it the top because,
        it is not going to contribute. 
        
        Finally, you go through the elements in nums1, if any element has a value in the dictionary, then return it, else,
        return -1.
        
        """

        stack = []
        ans = []
        d = dict()
        
        def peek(stack):
            if(len(stack)==0):
                return([])
            else:
                return(stack[-1])
            
        for i in range(len(nums2)):
            while(nums2[i]>peek(stack) and len(stack)>0):
                d[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        
        for i in nums1:
            ans.append(d.get(i,-1))
        
        return(ans)
            
                
                
