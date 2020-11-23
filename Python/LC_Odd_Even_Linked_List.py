# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return(None)
        odd = head
        even = head.next
        evenhead = even
        
        while(even!=None and even.next!=None):
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        #to link the odd and even togther. Because odd will be 1,3,5 and even will be 2,4. 
        #So you're pointing the odd.next which is 5.next to this evenhead which is 2. 
        odd.next = evenhead
        return(head)
            
