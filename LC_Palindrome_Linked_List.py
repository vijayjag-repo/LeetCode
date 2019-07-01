# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#   Approach:
#   Find the middle element using fast, slow pointers
#   Reverse the second half of elements. Either use stack in you're okay about using space. Else, reverse it using pointers.
#   Compare to check if each element is the same. Else, return False.

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return(True)
        
        #Finding the middle element
        fast = slow = curr = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
        
        #appending the second half to stack. When you pop() you get the reversed order
        stack = [slow.val]
        while(slow.next):
            slow = slow.next
            stack.append(slow.val)
        
        #Comparing the first and second halves.
        while(stack):
            if(stack.pop()!=curr.val):
                return(False)
            curr = curr.next
        
        return(True)
            
  
        
