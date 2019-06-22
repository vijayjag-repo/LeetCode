# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return(None)
        
        dup = head.val
        current = head
        
        while(current!=None and current.next!=None):
            if(current.next.val==dup):
                current.next = current.next.next
            else:
                dup = current.next.val
                current = current.next
        
        return(head)
        
