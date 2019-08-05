# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Approach:
        
        Same as Add Two Numbers but use stack to add from the end.
        """
        stack1 = []
        stack2 = []
        stack3 = []
        p1 = l1
        p2 = l2
        carry = 0
        dummy = head = ListNode(-1)
        
        while(p1):
            stack1.append(p1.val)
            p1 = p1.next
        while(p2):
            stack2.append(p2.val)
            p2 = p2.next
            
        while(stack1 or stack2 or carry):
            if(stack1):
                carry+=stack1.pop()
            if(stack2):
                carry+=stack2.pop()
            
            stack3.append(carry%10)
            carry/=10
            
        while(stack3):
            dummy.next = ListNode(stack3.pop())
            dummy = dummy.next
        return(head.next)
        
        
