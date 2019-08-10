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
        
        dummy = current = ListNode(-1)
        dummy.next = head
        
        while(head and head.next):
            if(head.val==head.next.val):
                while(head and head.next and head.val==head.next.val):
                    head = head.next
                head = head.next
                current.next = head
            else:
                current = current.next
                head = head.next
        return(dummy.next)
