from Queue import *
import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        
        Approach:
        
        Initialise a priority queue.
        Store the head's of the k lists.
        Get the least of them using get().
        Keep doing this.
        Finally return the pointer to the start.
        """
        curr = dummy = ListNode(-1)
        q = PriorityQueue()
        for node in lists:
            if(node):
                q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: 
                q.put((curr.next.val, curr.next))
        return dummy.next
    
# Using heap
import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        curr = dummy = ListNode(-1)
        h = [(node.val,node) for node in lists if node]
        heapq.heapify(h)
        while(h):
            value,node = h[0]
            if(not node.next):
                heapq.heappop(h)
            else:
                heapq.heapreplace(h,(node.next.val,node.next))
            curr.next = node
            curr = curr.next
        return(dummy.next)
