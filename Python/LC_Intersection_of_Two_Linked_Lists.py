# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        
        Approach:
        
        Crucial point in this problem is that, the difference in length can be countered by switching head.
        If both the pointers run till the end, we return null.
        If one pointer reaches the end before the other one, we know there's a difference in length.
        Therefore we set it to head of the other list which is shorter in length. 
        In the coming iterations, at some point, both pointers will run at the same time.
        If both pointers point to the same thing, we return that node.
        
        """
        if(headA and headB):
            a,b = headA,headB
            while(a!=b):
                a = a.next if a else headB
                b = b.next if b else headA

            return(a)
        
        
