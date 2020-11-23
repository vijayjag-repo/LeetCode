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
        
        Approach:
        
        Straightforward approach where you check if you encounter a node which you've already seen.
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
        
        Approach:
        
        Slow and Fast Runners.
        If the list is a cycle, then consider the list to be a circular track.
        If two runners of different speeds run, then they are bound to meet at some point.
        If they meet, return True
        If there is no cycle present, then the first runner would complete the race ie: there is only a finite distance to run.
        """
        if not head:
            return False
        slow = head
        fast = head.next
        
        while(slow!=fast):
            if(fast==None or fast.next==None):
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
            
    
        
        
        
