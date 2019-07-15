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
        
        As long as l1,l2 and carry exists, keep adding and simultaneously find the carry to be added next time.
        
        """
        curr = dummy = ListNode(-1)
        carry = 0
        while(l1 or l2 or carry):
            if(l1):
                carry+=l1.val
                l1 = l1.next
            if(l2):
                carry+=l2.val
                l2 = l2.next
            
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry/=10
            
        return(dummy.next)
