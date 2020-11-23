# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        
        Approach:
        
        Remember to visualise or draw.
        To go from pre -> a -> b -> b.next to pre -> b -> a -> b.next, we need to change those three references.
        After the first reversal is done, the next pre is set to a to continue the pattern for the remaining node elements.
        """
        
        dummy = pre = ListNode(0)
        pre.next = head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next,a.next,b.next = b,b.next,a
            pre = a
        return(dummy.next)
