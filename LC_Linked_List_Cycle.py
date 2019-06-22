# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return(False)
        while(head.next):
            if(head.val!='seen'):
                head.val = 'seen'
                head = head.next
            else:
                return(True)
        return(False)
        
        
        
